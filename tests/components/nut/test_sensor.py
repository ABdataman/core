"""The sensor tests for the nut platform."""

from homeassistant.const import PERCENTAGE
from homeassistant.helpers import entity_registry as er

from .util import async_init_integration


async def test_pr3000rt2u(hass):
    """Test creation of PR3000RT2U sensors."""

    await async_init_integration(hass, "PR3000RT2U", ["battery.charge"])
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == "CPS_PR3000RT2U_PYVJO2000034_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_cp1350c(hass):
    """Test creation of CP1350C sensors."""

    config_entry = await async_init_integration(hass, "CP1350C", ["battery.charge"])

    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_5e850i(hass):
    """Test creation of 5E850I sensors."""

    config_entry = await async_init_integration(hass, "5E850I", ["battery.charge"])
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_5e650i(hass):
    """Test creation of 5E650I sensors."""

    config_entry = await async_init_integration(hass, "5E650I", ["battery.charge"])
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_backupsses600m1(hass):
    """Test creation of BACKUPSES600M1 sensors."""

    await async_init_integration(hass, "BACKUPSES600M1", ["battery.charge"])
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert (
        entry.unique_id
        == "American Power Conversion_Back-UPS ES 600M1_4B1713P32195 _battery.charge"
    )

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_cp1500pfclcd(hass):
    """Test creation of CP1500PFCLCD sensors."""

    config_entry = await async_init_integration(
        hass, "CP1500PFCLCD", ["battery.charge"]
    )
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_dl650elcd(hass):
    """Test creation of DL650ELCD sensors."""

    config_entry = await async_init_integration(hass, "DL650ELCD", ["battery.charge"])
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_blazer_usb(hass):
    """Test creation of blazer_usb sensors."""

    config_entry = await async_init_integration(hass, "blazer_usb", ["battery.charge"])
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"

    state = hass.states.get("sensor.ups1_battery_charge")
    assert state.state == "100"

    expected_attributes = {
        "device_class": "battery",
        "friendly_name": "Ups1 Battery Charge",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )


async def test_stale_options(hass):
    """Test creation of sensors with stale options to remove."""

    config_entry = await async_init_integration(
        hass, "blazer_usb", ["battery.charge"], True
    )
    registry = er.async_get(hass)
    entry = registry.async_get("sensor.ups1_battery_charge")
    assert entry
    assert entry.unique_id == f"{config_entry.entry_id}_battery.charge"
    assert config_entry.options == {}
