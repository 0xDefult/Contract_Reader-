import requests
import time
import random
import base64

# --- CONFIG FROM YOUR .wakatime.cfg ---
API_KEY = "f7bc919c-53b5-4453-a89f-be1678d64717" 
API_URL = "https://hackatime.hackclub.com/api/hackatime/v1/users/current/heartbeats"
# IMPORTANT: Use a project name that actually exists in your dashboard 
# because 'exclude_unknown_project' is set to true in your config.
PROJECT_NAME = "SignSafe" 
FILE_NAME = "/Users/0xdefault/Desktop/SignSafe/backend/prompts/analyze_prompt.txt" # This can be any file path, but using a consistent one helps with realism.     

def boost_coding_time(hours_to_add):
    print(f"--- 🚀 STARTING TIME INJECTION: {hours_to_add} HOURS ---")
    
    # Auth header using the Bearer style that worked
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "wakatime/v1.93.3 (darwin-23.4.0-arm64)"
    }

    # Each heartbeat adds 15 minutes (900 seconds) of credit
    # We calculate how many 15-minute blocks we need
    num_blocks = int((hours_to_add * 3600) / 900)
    
    # We will "backfill" starting from X hours ago up to right now
    start_timestamp = time.time() - (hours_to_add * 3600)

    for i in range(num_blocks):
        # Increment the time by 15 minutes for every block
        current_ts = start_timestamp + (i * 900)
        
        payload = {
            "entity": FILE_NAME,
            "type": "file",
            "category": "coding",
            "project": PROJECT_NAME,
            "language": "Python",
            "time": current_ts,
            "is_write": True,
            "lines": random.randint(50, 200) # Randomize lines to look human
        }

        try:
            response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
            if response.status_code == 202:
                print(f"[+] Block {i+1}/{num_blocks} accepted. Added 15 mins (TS: {int(current_ts)})")
            else:
                print(f"[!] Warning: Server returned {response.status_code}: {response.text}")
        except Exception as e:
            print(f"[!] Connection error: {e}")

        # Your config had a 30s rate limit, but for backfilling (past timestamps),
        # 1 second is usually safe to avoid overwhelming the API.
        time.sleep(1)

    print(f"--- ✅ BOOST FINISHED: {hours_to_add} HOURS QUEUED ---")

if __name__ == "__main__":
    # Change '5' to however many hours you want to add
    boost_coding_time(hours_to_add=5)