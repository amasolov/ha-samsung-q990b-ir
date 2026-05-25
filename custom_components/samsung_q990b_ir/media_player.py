"""Media player platform for Samsung HW-Q990B IR integration."""

from __future__ import annotations

from homeassistant.components.media_player import (
    MediaPlayerDeviceClass,
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_INFRARED_ENTITY_ID
from .entity import Q990BIrEntity
from .ir_codes import Q990BCode

PARALLEL_UPDATES = 1


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Samsung Q990B IR media player from config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities([Q990BMediaPlayer(entry, infrared_entity_id)])


class Q990BMediaPlayer(Q990BIrEntity, MediaPlayerEntity):
    """Samsung HW-Q990B soundbar controlled via IR."""

    _attr_name = None
    _attr_assumed_state = True
    _attr_device_class = MediaPlayerDeviceClass.SPEAKER
    _attr_supported_features = (
        MediaPlayerEntityFeature.TURN_ON
        | MediaPlayerEntityFeature.TURN_OFF
        | MediaPlayerEntityFeature.VOLUME_STEP
        | MediaPlayerEntityFeature.VOLUME_MUTE
        | MediaPlayerEntityFeature.PLAY
        | MediaPlayerEntityFeature.PAUSE
        | MediaPlayerEntityFeature.SELECT_SOUND_MODE
        | MediaPlayerEntityFeature.SELECT_SOURCE
    )
    _attr_sound_mode_list = ["Standard", "Surround", "Game", "Adaptive"]
    _attr_source_list = ["HDMI", "Optical", "Bluetooth", "Wi-Fi"]

    def __init__(self, entry: ConfigEntry, infrared_entity_id: str) -> None:
        super().__init__(entry, infrared_entity_id, unique_id_suffix="media_player")
        self._attr_state = MediaPlayerState.ON
        self._attr_is_volume_muted = False

    async def async_turn_on(self) -> None:
        """Turn on the soundbar."""
        await self._send_command(Q990BCode.POWER)

    async def async_turn_off(self) -> None:
        """Turn off the soundbar."""
        await self._send_command(Q990BCode.POWER)

    async def async_volume_up(self) -> None:
        """Volume up."""
        await self._send_command(Q990BCode.VOLUME_UP)

    async def async_volume_down(self) -> None:
        """Volume down."""
        await self._send_command(Q990BCode.VOLUME_DOWN)

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute/unmute (toggle)."""
        await self._send_command(Q990BCode.MUTE)
        self._attr_is_volume_muted = not self._attr_is_volume_muted
        self.async_write_ha_state()

    async def async_select_source(self, source: str) -> None:
        """Cycle source input."""
        await self._send_command(Q990BCode.SOURCE)
        self._attr_source = source
        self.async_write_ha_state()

    async def async_select_sound_mode(self, sound_mode: str) -> None:
        """Cycle sound mode."""
        await self._send_command(Q990BCode.SOUND_MODE)
        self._attr_sound_mode = sound_mode
        self.async_write_ha_state()

    async def async_media_play(self) -> None:
        """Play."""
        await self._send_command(Q990BCode.PLAY_PAUSE)

    async def async_media_pause(self) -> None:
        """Pause."""
        await self._send_command(Q990BCode.PLAY_PAUSE)
