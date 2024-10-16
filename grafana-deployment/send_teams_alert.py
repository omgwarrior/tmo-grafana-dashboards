import requests
import json
import sys

def send_teams_alert(webhook_url, message):
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": message
    }

    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print("Alert sent successfully to Microsoft Teams.")
        else:
            print(f"Failed to send alert. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending alert: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python send_teams_alert.py <webhook_url> <message>")
        sys.exit(1)

    webhook_url = sys.argv[1]
    message = sys.argv[2]
    send_teams_alert(webhook_url, message)
