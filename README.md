# 🌐 website change monitor

## 🔍 overview
this script monitors a specified website for content changes and sends a notification via a webhook if any changes are detected.

## ✨ features
- fetches website content and computes an md5 hash to detect changes.
- sends a notification to a webhook when a change is detected.
- runs continuously with a customizable check interval.

## 📦 requirements
- python 3.x
- `requests`
- `python-dotenv`

## ⚙️ installation
1. clone this repository or download the script.
2. install dependencies:
   ```sh
   pip install requests python-dotenv
   ```
3. create a `.env` file and define the following environment variables:
   ```env
   url=https://example.com  # the website url to monitor
   webhook=https://your-webhook-url  # webhook url for notifications
   ```

## 🚀 usage
run the script with:
```sh
python script.py
```
the script will check the website every 60 seconds by default.

## 🎛️ customization
you can modify the `check_interval` parameter in `monitor_website(url, check_interval=60)` to adjust how frequently the script checks for changes.

## ⚠️ notes
- ensure the website you are monitoring allows automated requests.
- use a webhook service like discord, slack, or a custom server to receive notifications.

## 📜 license
mit license. feel free to modify and use! 🎉


