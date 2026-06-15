#!/bin/bash

# 1. Variables
LOG="server_incident.log"
REPORT="incident_report.txt"

# Clear the old report if it exists
> "$REPORT"

echo "--------------------------------------------------"
echo "    INCIDENT RESPONSE ANALYSIS IN PROGRESS..."
echo "--------------------------------------------------"

# 2. Logic: Brute Force & Success Detection
# We first find IPs with > 2 failed attempts (401)
FAILED_IPS=$(grep " 401 " "$LOG" | awk '{print $1}' | sort | uniq -c | awk '$1 > 2 {print $2}')

for IP in $FAILED_IPS; do
    # Count total failures for this specific IP
    COUNT=$(grep " 401 " "$LOG" | grep "$IP" | wc -l)
    
    # Check if this specific IP ever got a 200 after those failures
    if grep "$IP" "$LOG" | grep -q " 200 "; then
        STATUS="COMPROMISED"
    else
        STATUS="ATTEMPTED"
    fi
    
    # Append to the report file
    echo "IP: $IP | Failures: $COUNT | Status: $STATUS" >> "$REPORT"
done

# 3. Logic: Forbidden Access (/admin with 403)
# We find IPs hitting /admin and getting a 403
FORBIDDEN_IPS=$(grep " 403 " "$LOG" | grep "/admin" | awk '{print $1}' | sort -u)

for IP in $FORBIDDEN_IPS; do
    # Check if they are already in the report to avoid duplicates
    if ! grep -q "$IP" "$REPORT"; then
        echo "IP: $IP | Access: Forbidden (/admin) | Status: ATTACKER" >> "$REPORT"
    fi
done

echo "[+] Analysis complete. Review $REPORT for details."








