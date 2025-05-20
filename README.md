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

## ❤️ Credits

Built with 💧 by the Home Assistant + GrowCube community.

---

## ☕ Support This Project

If you found this useful, you can support future work here:

<a href="https://buymeacoffee.com/dstasiak" target="_blank">
  <img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-%23FFDD00.svg?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
</a>

---
