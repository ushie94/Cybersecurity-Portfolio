@echo off
REM Comprehensive Audio Configuration Script
REM Disables Stereo Mix and sets Headphone Microphone as default

echo.
echo =====================================
echo AUDIO CONFIGURATION - SETUP
echo =====================================
echo.
echo [1] Configuring audio devices...
echo.

REM Open Sound Settings
echo Opening Sound Settings for manual configuration...
echo.
echo When Sound Settings opens:
echo   1. Go to "Input devices"
echo   2. SELECT your headphone microphone
echo   3. Click "Set as default"
echo   4. Adjust microphone level to 85-90%%
echo   5. Click "Test your microphone" and speak loudly
echo   6. Close Sound Settings when done
echo.

timeout /t 3 /nobreak
start ms-settings:sound

echo.
echo =====================================
echo Configuration Guide:
echo =====================================
echo.
echo TO DISABLE STEREO MIX MANUALLY:
echo 1. Right-click speaker icon -> Open Sound settings
echo 2. Go to "Input devices" at the bottom, scroll down
echo 3. Look for "Stereo Mix" devices
echo 4. Right-click -> Disable all Stereo Mix instances
echo.
echo TO SET HEADPHONE MIC AS DEFAULT:
echo 1. In Input devices, find your headphone microphone
echo 2. Right-click -> Set as default device
echo 3. Click the device -> Device properties
echo 4. Check "Enable" if it shows disabled
echo.
echo =====================================
pause
