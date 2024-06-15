import requests
import time
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

# URL of the website to monitor
url = os.getenv("url")
# URL of the webhook
webhook_url = os.getenv("webhook")

# Function to get the hash of the website content


def get_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

# Function to get the website content


def get_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to send a notification to the webhook


def send_webhook_notification(message):
    payload = {"text": message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification: {response.status_code}")
        print(f"Response content: {response.text}")

# Monitor the website for changes


def monitor_website(url, check_interval=60):
    initial_content = get_website_content(url)
    if initial_content is None:
        print("Failed to retrieve the initial content.")
        return

    initial_hash = get_hash(initial_content)
    print("Monitoring started...")

    while True:
        time.sleep(check_interval)
        current_content = get_website_content(url)
        if current_content is None:
            print("Failed to retrieve the current content.")
            continue

        current_hash = get_hash(current_content)
        if current_hash != initial_hash:
            print("Change detected on the website!")
            send_webhook_notification("Change detected on the website!")
            initial_hash = current_hash  # Update the hash to the new content
        else:
            print("No change detected.")


if __name__ == "__main__":
    monitor_website(url, check_interval=60)
