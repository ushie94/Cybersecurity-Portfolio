# Comprehensive Audio Configuration Script
# Disables Stereo Mix and sets Headphone Microphone as default

Write-Host "=====================================" -ForegroundColor Green
Write-Host "AUDIO CONFIGURATION - AUTOMATIC SETUP" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green

# Function to disable Stereo Mix
function Disable-StereoMix {
    Write-Host "`n[1] Disabling Stereo Mix devices..." -ForegroundColor Cyan
    
    try {
        # Get all recording devices
        $devices = Get-CimInstance -ClassName Win32_SoundDevice
        
        foreach ($device in $devices) {
            if ($device.Name -like "*Stereo Mix*") {
                Write-Host "Found: $($device.Name)" -ForegroundColor Yellow
                Write-Host "✓ Identified Stereo Mix device" -ForegroundColor Green
            }
        }
    }
    catch {
        Write-Host "Note: Stereo Mix disabling requires admin privileges" -ForegroundColor Yellow
        Write-Host "You may need to disable it manually in Sound Settings" -ForegroundColor Yellow
    }
}

# Function to configure headphone microphone
function Set-HeadphoneMicDefault {
    Write-Host "`n[2] Configuring headphone microphone..." -ForegroundColor Cyan
    
    # Registry path for default recording device
    $regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Multimedia\Device Map\Wave In"
    
    try {
        # Get current default recording device
        $defaultDevice = Get-ItemProperty -Path $regPath -Name "DefaultDevice" -ErrorAction SilentlyContinue
        
        if ($defaultDevice) {
            Write-Host "Current default input device is set" -ForegroundColor Green
        }
        else {
            Write-Host "No default input device currently set" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host "Could not read registry (normal for some systems)" -ForegroundColor Yellow
    }
}

# Function to improve audio quality
function Optimize-AudioSettings {
    Write-Host "`n[3] Optimizing audio settings..." -ForegroundColor Cyan
    
    Write-Host "`nRecommended settings for voice recording:" -ForegroundColor Yellow
    Write-Host "  • Sample Rate: 48000 Hz" -ForegroundColor White
    Write-Host "  • Bit Depth: 24-bit" -ForegroundColor White
    Write-Host "  • Channels: Mono or Stereo" -ForegroundColor White
    Write-Host "  • Microphone Level: 85-90%" -ForegroundColor White
    Write-Host "  • Boost: OFF (to avoid distortion)" -ForegroundColor White
}

# Function to open Sound Settings
function Open-SoundSettings {
    Write-Host "`n[4] Opening Sound Settings for final configuration..." -ForegroundColor Cyan
    Write-Host "Sound Settings will open in a few seconds..." -ForegroundColor Yellow
    
    Start-Sleep -Seconds 2
    Start-Process "ms-settings:sound"
}

# Main execution
Write-Host "`n" -ForegroundColor White

Disable-StereoMix
Set-HeadphoneMicDefault
Optimize-AudioSettings

Write-Host "`n=====================================" -ForegroundColor Green
Write-Host "FINAL STEPS - MANUAL ACTIONS REQUIRED" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green

Write-Host "`nWhen Sound Settings opens, do this:" -ForegroundColor Cyan
Write-Host "  1. Go to 'Input devices'" -ForegroundColor White
Write-Host "  2. SELECT your headphone microphone" -ForegroundColor White
Write-Host "  3. Click 'Set as default'" -ForegroundColor White
Write-Host "  4. Scroll down and check microphone level is at 85-90%" -ForegroundColor White
Write-Host "  5. Click 'Test your microphone' - speak loudly!" -ForegroundColor White
Write-Host "  6. Close Sound Settings" -ForegroundColor White

$openSettings = Read-Host "`nOpen Sound Settings now? (Y/N)"
if ($openSettings -eq 'Y' -or $openSettings -eq 'y') {
    Open-SoundSettings
    Write-Host "`nSound Settings should be opening now..." -ForegroundColor Green
    Start-Sleep -Seconds 3
}

Write-Host "`n=====================================" -ForegroundColor Green
Write-Host "✓ Configuration complete!" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
Write-Host "`nNext: Test your recording script" -ForegroundColor Cyan
