"""Diagnostics support for Open-Meteo."""
from __future__ import annotations

import json
from typing import Any

from open_meteo import Forecast

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN

TO_REDACT = {
    CONF_LATITUDE,
    CONF_LONGITUDE,
}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator: DataUpdateCoordinator[Forecast] = hass.data[DOMAIN][entry.entry_id]
    # Round-trip via JSON to trigger serialization
    data: dict[str, Any] = json.loads(coordinator.data.json())
    return async_redact_data(data, TO_REDACT)
