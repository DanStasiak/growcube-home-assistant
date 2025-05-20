# GrowCube Home Assistant Automation

A complete GrowCube auto-watering system for Home Assistant.

## Features

- 🌱 Moisture-based watering with thresholds
- 🔁 Adjustable watering cycle + dry-run mode
- 📊 Per-plant logging with daily/weekly summaries
- 💬 Notifications via email/mobile
- 📈 Lovelace UI view with summaries
- 🧠 Powered by `pyscript.set_state`

## Installation

1. Copy folders to your Home Assistant `/config/` directory:
   - `blueprints/automation/`
   - `scripts/`
   - `automations/`
   - `sensors/`
   - `pyscript/`
   - `lovelace/`

2. In `configuration.yaml`, include:
```yaml
automation: !include automations.yaml
script: !include scripts.yaml
sensor: !include_dir_merge_list sensors/
python_script:
pyscript:
lovelace:
  mode: yaml
```

3. Restart Home Assistant.
4. Import the blueprint from:
   `blueprints/automation/growcube_auto_water_blueprint.yaml`
5. Add Lovelace view:
```yaml
- !include lovelace/view_growcube_logs.yaml
```

Enjoy automated plant care! 🌿
