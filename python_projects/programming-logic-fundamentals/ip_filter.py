        # Project: SOC IP Validator & Sanitizer
# Purpose: Filters internal traffic and flags invalid IP strings.

ip_addresses = ["192.168.1.1", "10.0.0.1", "256.0.0.1", "192.168.1.256", "8.8.8.8"]

for ip in ip_addresses:
    # Logic: Split the IP by dots and check if any part is over 255
    parts = ip.split(".")
    is_valid = all(0 <= int(p) <= 255 for p in parts if p.isdigit()) and len(parts) == 4

    if not is_valid:
        print(f"[!] {ip} is INVALID - POSSIBLE MALICIOUS DATA")
    elif ip.startswith("192.168"):
        print(f"[✓] {ip} is INTERNAL - ALLOW")
    else:
        print(f"[?] {ip} is EXTERNAL - MONITOR")