"""Support for the Environment Canada weather service."""
from datetime import datetime, timedelta
import logging
import re

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import (
    ATTR_ATTRIBUTION,
    ATTR_LOCATION,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    DEVICE_CLASS_TEMPERATURE,
    TEMP_CELSIUS,
)
import homeassistant.helpers.config_validation as cv

from . import trigger_import
from .const import ATTR_STATION, CONF_ATTRIBUTION, CONF_LANGUAGE, CONF_STATION, DOMAIN

SCAN_INTERVAL = timedelta(minutes=10)
ATTR_UPDATED = "updated"
ATTR_TIME = "alert time"

_LOGGER = logging.getLogger(__name__)


def validate_station(station):
    """Check that the station ID is well-formed."""
    if station is None:
        return None
    if not re.fullmatch(r"[A-Z]{2}/s0000\d{3}", station):
        raise vol.error.Invalid('Station ID must be of the form "XX/s0000###"')
    return station


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_LANGUAGE, default="english"): vol.In(["english", "french"]),
        vol.Optional(CONF_STATION): validate_station,
        vol.Inclusive(CONF_LATITUDE, "latlon"): cv.latitude,
        vol.Inclusive(CONF_LONGITUDE, "latlon"): cv.longitude,
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Environment Canada sensor."""
    trigger_import(hass, config)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add a weather entity from a config_entry."""
    weather_data = hass.data[DOMAIN][config_entry.entry_id]["weather_data"]
    sensor_list = list(weather_data.conditions) + list(weather_data.alerts)

    async_add_entities(
        [
            ECSensor(
                sensor_type,
                f"{config_entry.title} {sensor_type}",
                weather_data,
                f"{weather_data.metadata['location']}-{sensor_type}",
            )
            for sensor_type in sensor_list
        ],
        True,
    )


class ECSensor(SensorEntity):
    """Implementation of an Environment Canada sensor."""

    def __init__(self, sensor_type, name, ec_data, unique_id):
        """Initialize the sensor."""
        self.sensor_type = sensor_type
        self.ec_data = ec_data

        self._attr_unique_id = unique_id
        self._attr_name = name
        self._state = None
        self._attr = None
        self._unit = None
        self._device_class = None

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the device."""
        return self._attr

    @property
    def native_unit_of_measurement(self):
        """Return the units of measurement."""
        return self._unit

    @property
    def device_class(self):
        """Return the class of this device, from component DEVICE_CLASSES."""
        return self._device_class

    def update(self):
        """Update current conditions."""
        self.ec_data.update()
        self.ec_data.conditions.update(self.ec_data.alerts)

        conditions = self.ec_data.conditions
        metadata = self.ec_data.metadata
        sensor_data = conditions.get(self.sensor_type)

        self._attr = {}
        value = sensor_data.get("value")

        if isinstance(value, list):
            self._state = " | ".join([str(s.get("title")) for s in value])[:255]
            self._attr.update(
                {ATTR_TIME: " | ".join([str(s.get("date")) for s in value])}
            )
        elif self.sensor_type == "tendency":
            self._state = str(value).capitalize()
        elif value is not None and len(value) > 255:
            self._state = value[:255]
            _LOGGER.info(
                "Value for %s truncated to 255 characters", self._attr_unique_id
            )
        else:
            self._state = value

        if sensor_data.get("unit") == "C" or self.sensor_type in (
            "wind_chill",
            "humidex",
        ):
            self._unit = TEMP_CELSIUS
            self._device_class = DEVICE_CLASS_TEMPERATURE
        else:
            self._unit = sensor_data.get("unit")

        timestamp = metadata.get("timestamp")
        if timestamp:
            updated_utc = datetime.strptime(timestamp, "%Y%m%d%H%M%S").isoformat()
        else:
            updated_utc = None

        self._attr.update(
            {
                ATTR_ATTRIBUTION: CONF_ATTRIBUTION,
                ATTR_UPDATED: updated_utc,
                ATTR_LOCATION: metadata.get("location"),
                ATTR_STATION: metadata.get("station"),
            }
        )
