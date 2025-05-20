# 🌿 GrowCube Home Assistant Integration

[![hass-version](https://img.shields.io/badge/Home%20Assistant-2024.5+-blue?logo=home-assistant)](https://www.home-assistant.io)
[![license](https://img.shields.io/github/license/DanStasiak/growcube-home-assistant)](LICENSE)

This is a fully featured Home Assistant automation package for the [GrowCube](https://www.gardena.com/int/products/smart/irrigation/growcube/) smart plant watering system. It includes:

- ✅ Automatic moisture-based plant watering
- 📊 Logging with per-plant stats
- 📨 Email + push notifications
- 🗓️ Daily & weekly summary reports
- 📈 Lovelace view for visualization
- 💾 Modular YAML + Pyscript logic

---

## 🚀 Quick Start

### 📘 Blueprint Import

Paste this in your Home Assistant:

```
https://raw.githubusercontent.com/DanStasiak/growcube-home-assistant/main/blueprints/automation/growcube_auto_water_blueprint.yaml
```

Then go to:  
**Settings → Automations & Scenes → Blueprints → Import Blueprint**

---

## 📁 Included Components

```text
📂 blueprints/
  └── automation/growcube_auto_water_blueprint.yaml
📂 scripts/
  └── log_growcube_watering.yaml
📂 automations/
  ├── growcube_daily_summary.yaml
  ├── growcube_weekly_summary.yaml
  └── growcube_reset_daily.yaml
📂 sensors/
  └── growcube_watering_log.yaml
📂 pyscript/
  └── set_state.py
📂 lovelace/
  └── view_growcube_logs.yaml
📄 README.md
```

---

## 🛠 Installation

1. Copy these folders to your Home Assistant `/config/` directory:
    - `blueprints/`
    - `scripts/`
    - `automations/`
    - `sensors/`
    - `pyscript/`
    - `lovelace/`

2. Add or update your `configuration.yaml`:

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

4. Import the blueprint and create automations for each plant.

5. Add the Lovelace view to `ui-lovelace.yaml`:

```yaml
- !include lovelace/view_growcube_logs.yaml
```

---

## 📸 Screenshots
<details>
  <summary>📊 Watering Logs complete</summary>
  <img src="https://github.com/DanStasiak/growcube-home-assistant/assets/log_screenshot.png" width="600">
</details>

<details>
  <summary>🌱 Today’s Log</summary>
  <img src="https://github.com/DanStasiak/growcube-home-assistant/assets/preview-today.png" width="600">
</details>

<details>
  <summary>📊 Watering Summary</summary>
  <img src="https://github.com/DanStasiak/growcube-home-assistant/assets/preview-summary.png" width="600">
</details>

---

## 📬 Notifications

You’ll receive:
- Email summaries daily & weekly
- Mobile push per watering cycle
- Water tank empty alerts

---

## 🤝 Contributing

Feel free to fork, improve or submit a pull request.
Questions? Join the conversation on the [Home Assistant Forum](https://community.home-assistant.io/c/blueprints-exchange/).

---

**Enjoy your smart plants! 🌿**

## ❤️ Credits

Built with 💧 by the Home Assistant + GrowCube community.

---

## ☕ Support This Project

If you found this useful, you can support future work here:

<a href="https://buymeacoffee.com/dstasiak" target="_blank">
  <img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-%23FFDD00.svg?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
</a>

---
