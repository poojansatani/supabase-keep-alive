import os
import requests

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_ANON_KEY"]

url = f"{SUPABASE_URL}/rest/v1/app_users?select=*&limit=1"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)
print(response.text)
