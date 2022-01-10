"""The zcc integration."""
from __future__ import annotations

import logging
import pprint

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr

from .const import CONTROLLER, DOMAIN, PLATFORMS
from .controller import ZimiController

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setup Zimi Controller from config entry"""

    _LOGGER.info("Starting async_setup_entry")
    _LOGGER.info("entry_id: %s" % entry.entry_id)
    _LOGGER.info("data:     %s" % pprint.pformat(entry.data))
    controller = ZimiController(hass, entry)
    connected = controller.connect()
    if not connected:
        return False

    hass.data[CONTROLLER] = controller

    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, controller.api.mac)},
        manufacturer=controller.api.brand,
        name=f"Zimi({controller.api.host}:{controller.api.port})",
        model=controller.api.product,
        sw_version="unknown",
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
