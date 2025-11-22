# Roblox Group Finder

A lightweight Python script that scans Roblox group IDs to find **unowned**, **unlocked**, and **claimable** groups — and automatically sends notifications to a Discord webhook.

This tool continuously checks random group IDs and alerts you when it finds a group that:

* Has **no owner**
* Is **public entry allowed**
* Is **not locked**

Useful for Roblox group hunters and automation enthusiasts.

---

## 🚀 Features

* Scans thousands of Roblox groups using random IDs
* Detects groups that are unclaimed & open
* Sends detailed info to a Discord webhook:

  * Group ID
  * Description
  * Member count
  * Direct group link
* Color-coded terminal output (found vs not found)
* Infinite scanner loop

---

## 📦 Requirements

* Python 3.8+
* `requests`
* `discord_webhook`

Install dependencies:

```bash
pip install requests discord_webhook
```

---

## 💡 Usage

Run the script:

```bash
python groupfinder.py
```

The script will begin scanning random Roblox group IDs within this range:

```
10800000 - 10960000
```

You can modify this range directly in the code.

When an unclaimed group is found, it will be sent to your configured Discord Webhook.

---

## ⚙️ Configuration

Replace the webhook URL inside the script:

```python
webhook = DiscordWebhook(url="YOUR_WEBHOOK_HERE")
```

To adjust the scan range:

```python
ID = random.randint(START_ID, END_ID)
```

---

## 🛑 Disclaimer

This project is for **educational purposes**.
Automated scanning and webhook reporting may violate Roblox or Discord ToS if misused.
Use responsibly — you are fully responsible for how you use this tool.

---

## 📄 License

MIT License — free to use, modify, and distribute.
