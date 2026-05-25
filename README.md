# Samsung HW-Q990B Infrared for Home Assistant

[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

Control a **Samsung HW-Q990B** soundbar over infrared using Home Assistant's
native [infrared entity platform](https://www.home-assistant.io/integrations/infrared/) (HA 2026.4+).

The integration sends raw IR commands through any configured infrared emitter
(ESPHome IR blaster, Broadlink RM, etc.), giving you a **media player** entity
and **15 button** entities for every key on the AH81-09773A remote.

## Requirements

| Requirement | Version |
|---|---|
| Home Assistant | 2026.4 or later |
| Infrared emitter | Any entity on the `infrared` platform |

Your emitter device must expose an `infrared` entity in Home Assistant
(e.g. ESPHome IR proxy, Broadlink RM Max custom integration).

## Installation

### HACS (recommended)

1. Open **HACS &rarr; Integrations &rarr; ⋮ &rarr; Custom repositories**
2. Add `https://github.com/amasolov/ha-samsung-q990b-ir` as an **Integration**
3. Search for **Samsung HW-Q990B Infrared** and click **Download**
4. Restart Home Assistant

### Manual

Copy `custom_components/samsung_q990b_ir/` into your Home Assistant
`config/custom_components/` directory and restart.

## Setup

1. Go to **Settings &rarr; Devices & Services &rarr; Add Integration**
2. Search for **Samsung HW-Q990B Infrared**
3. Select the infrared emitter entity that can reach your soundbar
4. Done — a device with a media player and button entities appears

## Entities

### Media Player

| Feature | Action |
|---|---|
| Turn on / off | Sends power toggle |
| Volume up / down | Sends volume IR commands |
| Mute | Toggles mute |
| Select source | Cycles input source |
| Select sound mode | Cycles sound mode |
| Play / Pause | Sends play/pause toggle |

### Buttons

| Button | Remote key |
|---|---|
| Power | Power toggle |
| Source | Input source cycle |
| Sound Mode | Sound mode cycle |
| Bass Up / Down | Subwoofer level |
| Bluetooth Pair | BT pairing mode |
| Info | Display info |
| Channel Level | Speaker level menu |
| Settings | Settings menu |
| Tone Control | EQ / tone menu |
| Play/Pause | Play/pause toggle |
| Up / Down / Left / Right | Navigation |

## IR Codes

Codes were learned from the Samsung AH81-09773A remote using a Broadlink RM Max.
They are stored as base64-encoded Broadlink IR packets and converted to raw
microsecond timings at runtime.

## License

MIT
