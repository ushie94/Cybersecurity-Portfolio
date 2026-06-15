import bz2
import json

COMPRESSED_FILE = "log_parsing_project/raw_windows/wls_day-71.bz2"

print("--- Active Directory Process Execution Monitor ---")

with bz2.open(COMPRESSED_FILE, "rt") as file:
    alert_count = 0
    limit = 5
    
    for line in file:
        # 1. Parse the JSON string into a usable Python dictionary
        try:
            log_data = json.loads(line.strip())
        except json.JSONDecodeError:
            continue # Skip any corrupted lines safely
            
        # 2. Extract our target keys
        event_id = log_data.get("EventID")
        user = log_data.get("UserName")
        process = log_data.get("ProcessName")
        host = log_data.get("LogHost")
        
        # 3. Security Logic: Flag Process Creation (Event ID 4688)
        if event_id == 4688:
            print(f"[PROCESS SECURITY ALERT] Host: {host} | User: {user} launched program: {process}")
            alert_count += 1
            
            if alert_count >= limit:
                print(f"\n--- Safely stopped after printing {limit} process alerts ---")
                break

print("--- Threat Hunt Complete ---")