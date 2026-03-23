# Project: Network Traffic Sanitizer
# Purpose: Validates and categorizes IP addresses for SOC analysis.

ip_addresses = [
    "192.168.1.1", "10.0.0.1", "8.8.8.8", 
    "192.168.1.256", "256.0.0.1", "172.16.0.1", 
    "192.168.1", "192.168.1.1.1", "not_an_ip"
]

print(f"{'IP ADDRESS':<20} | {'STATUS':<25}")
print("-" * 50)

for ip in ip_addresses:
    parts = ip.split(".")
    
    # Check if all parts are numbers and within the 0-255 range
    # and ensure there are exactly 4 parts.
    is_valid = (
        len(parts) == 4 and 
        all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
    )

    if not is_valid:
        status = "❌ INVALID DATA"
    elif ip.startswith("192.168") or ip.startswith("10."):
        status = "✅ INTERNAL - ALLOW"
    else:
        status = "🔍 EXTERNAL - MONITOR"
        
    print(f"{ip:<20} | {status:<25}")