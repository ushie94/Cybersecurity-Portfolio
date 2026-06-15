import bz2

COMPRESSED_FILE = "log_parsing_project/raw_network/netflow_day-71.bz2"

print("--- Automated Firewall Traffic Analyzer ---")

with bz2.open(COMPRESSED_FILE, "rt") as file:
    match_count = 0
    limit = 5
    
    for line in file:
        # 1. Clean the line and split strictly by COMMAS
        parts = line.strip().split(",")
        
        # Safety check: ensure the line isn't empty and has enough fields
        if len(parts) < 7:
            continue
            
        source_device = parts[2]
        dest_device = parts[3]
        protocol = "TCP" if parts[4] == "6" else parts[4]
        dest_port = parts[6]
        
        # 2. Security Logic: Flag any traffic hitting Destination Port 80
        if dest_port == "80":
            print(f"[ALERT] Unencrypted Web Traffic! Connection: {source_device} -> {dest_device} over {protocol}/{dest_port}")
            match_count += 1
            
            if match_count >= limit:
                print(f"\n--- Stoppped early after finding {limit} alerts for demo purposes ---")
                break

print("--- Analysis Finished ---")