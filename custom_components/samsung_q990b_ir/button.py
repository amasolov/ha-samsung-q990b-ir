"""Button platform for Samsung HW-Q990B IR integration."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_INFRARED_ENTITY_ID
from .entity import Q990BIrEntity
from .ir_codes import Q990BCode

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class Q990BButtonDescription(ButtonEntityDescription):
    """Describes a Q990B IR button entity."""

    command_code: Q990BCode


BUTTON_DESCRIPTIONS: tuple[Q990BButtonDescription, ...] = (
    Q990BButtonDescription(
        key="power",
        name="Power",
        command_code=Q990BCode.POWER,
    ),
    Q990BButtonDescription(
        key="source",
        name="Source",
        command_code=Q990BCode.SOURCE,
    ),
    Q990BButtonDescription(
        key="sound_mode",
        name="Sound Mode",
        command_code=Q990BCode.SOUND_MODE,
    ),
    Q990BButtonDescription(
        key="bass_up",
        name="Bass Up",
        command_code=Q990BCode.BASS_UP,
    ),
    Q990BButtonDescription(
        key="bass_down",
        name="Bass Down",
        command_code=Q990BCode.BASS_DOWN,
    ),
    Q990BButtonDescription(
        key="bluetooth_pair",
        name="Bluetooth Pair",
        command_code=Q990BCode.BLUETOOTH_PAIR,
    ),
    Q990BButtonDescription(
        key="info",
        name="Info",
        command_code=Q990BCode.INFO,
    ),
    Q990BButtonDescription(
        key="ch_level",
        name="Channel Level",
        command_code=Q990BCode.CH_LEVEL,
    ),
    Q990BButtonDescription(
        key="settings",
        name="Settings",
        command_code=Q990BCode.SETTINGS,
    ),
    Q990BButtonDescription(
        key="tone_control",
        name="Tone Control",
        command_code=Q990BCode.TONE_CONTROL,
    ),
    Q990BButtonDescription(
        key="play_pause",
        name="Play/Pause",
        command_code=Q990BCode.PLAY_PAUSE,
    ),
    Q990BButtonDescription(
        key="up",
        name="Up",
        command_code=Q990BCode.UP,
    ),
    Q990BButtonDescription(
        key="down",
        name="Down",
        command_code=Q990BCode.DOWN,
    ),
    Q990BButtonDescription(
        key="left",
        name="Left",
        command_code=Q990BCode.LEFT,
    ),
    Q990BButtonDescription(
        key="right",
        name="Right",
        command_code=Q990BCode.RIGHT,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Samsung Q990B IR buttons from config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities(
        Q990BButton(entry, infrared_entity_id, desc)
        for desc in BUTTON_DESCRIPTIONS
    )


class Q990BButton(Q990BIrEntity, ButtonEntity):
    """Samsung Q990B IR button entity."""

    entity_description: Q990BButtonDescription

    def __init__(
        self,
        entry: ConfigEntry,
        infrared_entity_id: str,
        description: Q990BButtonDescription,
    ) -> None:
        super().__init__(entry, infrared_entity_id, unique_id_suffix=description.key)
        self.entity_description = description

    async def async_press(self) -> None:
        """Press the button."""
        await self._send_command(self.entity_description.command_code)
