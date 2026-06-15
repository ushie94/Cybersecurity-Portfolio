#!/bin/bash

# Configuration
LOG="access.log"
THREAT_FILE="threats.txt"
ADMIN_FILE="admin_access.log"

echo "--- SOC Health Check Started ---"

# 1. Check for Unauthorized Access (401/403)
if grep -qE "401|403" "$LOG"; then
    echo "[ALERT] Unauthorized access (401/403) detected!"
    grep -E "401|403" "$LOG" > "$THREAT_FILE"
    echo "Report generated: $THREAT_FILE"
else
    echo "[OK] No unauthorized access detected."
fi

# 2. Check for Admin Access
if grep -qE "/admin" "$LOG"; then
    echo "[ALERT] Admin access detected!"
    grep -E "/admin" "$LOG" > "$ADMIN_FILE"
    echo "Report generated: $ADMIN_FILE"
else
    echo "[OK] No /admin access attempts detected."
fi

# 3. Count Total Traffic
TOTAL_REQ=$(wc -l < "$LOG")
echo "Total requests processed: $TOTAL_REQ"

echo "--- SOC Health Check Complete ---"
