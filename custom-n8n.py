#!/usr/bin/env python3

import sys
import json

try:
    import requests
except ImportError:
    print("No module 'requests' found. Install: pip3 install requests")
    sys.exit(1)

# Read arguments
alert_file = sys.argv[1]
hook_url = sys.argv[3]

# Load alert JSON
try:
    with open(alert_file) as f:
        alert_json = json.loads(f.read())
except FileNotFoundError:
    print(f"File {alert_file} tidak ditemukan.")
    sys.exit(1)
except json.JSONDecodeError:
    print("File bukan JSON valid.")
    sys.exit(1)

# Build full payload (send all _source data)
payload = json.dumps(alert_json)

# Send to n8n webhook
r = requests.post(hook_url, data=payload, headers={"content-type": "application/json"})

if r.status_code != 200:
    print(f"Gagal mengirim alert: {r.status_code}, {r.text}")
    sys.exit(1)

sys.exit(0)
