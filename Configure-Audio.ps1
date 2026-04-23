# Audio Device Configuration Script
# Lists all audio devices and helps set default device

# Get all audio playback devices
Write-Host "=== Available Audio Output Devices ===" -ForegroundColor Green
$audioDevices = Get-CimInstance -ClassName Win32_SoundDevice

foreach ($device in $audioDevices) {
    Write-Host "- $($device.Name)" -ForegroundColor Cyan
}

Write-Host "`n=== Checking Default Playback Device ===" -ForegroundColor Green
$defaultDevice = Get-CimInstance -ClassName Win32_PnPDevice | Where-Object { $_.ConfigManagerErrorCode -eq 0 }
Write-Host "Current configuration detected. Check Sound Settings (Windows Settings > Sound > Advanced)"`

Write-Host "`n=== Instructions ===" -ForegroundColor Yellow
Write-Host "1. Run this command to open Sound Settings:"
Write-Host "   ms-settings:sound" -ForegroundColor Magenta
Write-Host "`n2. Under 'Advanced', set your headphone as default output"
Write-Host "3. Set microphone (if available) as default input"

# Offer to open Sound Settings
$response = Read-Host "`nOpen Sound Settings now? (Y/N)"
if ($response -eq 'Y' -or $response -eq 'y') {
    Start-Process "ms-settings:sound"
}
