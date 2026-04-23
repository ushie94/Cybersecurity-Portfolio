"""
Diagnostic script to identify which device is your external headphone microphone
"""

import sounddevice as sd
import numpy as np

def test_specific_device(device_id, duration=3, threshold=0.1):
    """
    Test a specific device to see if it's picking up external audio
    """
    print(f"\n{'='*60}")
    print(f"Testing Device {device_id}: {sd.query_devices()[device_id]['name']}")
    print(f"{'='*60}")
    print(f"Recording for {duration} seconds...")
    print("Speak LOUDLY into the headphone microphone now!")
    print("(or tap the microphone)")
    
    try:
        recording = sd.rec(int(44100 * duration), samplerate=44100, 
                          channels=1, device=device_id, dtype='float32')
        sd.wait()
        
        # Analyze audio
        max_level = np.max(np.abs(recording))
        mean_level = np.mean(np.abs(recording))
        
        print(f"\n📊 Results:")
        print(f"   Peak level: {max_level:.3f}")
        print(f"   Average level: {mean_level:.3f}")
        
        if max_level > threshold:
            print(f"✅ DETECTED AUDIO from this device!")
            if mean_level > 0.05:
                print(f"   This looks like your HEADPHONE MICROPHONE! 🎤")
                return True
            else:
                print(f"   ⚠️ This might be background noise or Stereo Mix")
                return False
        else:
            print(f"❌ NO AUDIO detected - this is NOT your headphone mic")
            return False
            
    except Exception as e:
        print(f"❌ Error testing device: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("HEADPHONE MICROPHONE DIAGNOSTIC")
    print("="*60)
    
    # Get all input devices
    devices = sd.query_devices()
    input_devices = []
    
    print("\nInput Devices Available:")
    print("-" * 60)
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            input_devices.append(i)
            print(f"{i}: {device['name']}")
            # Highlight potential microphone devices
            name_lower = device['name'].lower()
            if 'microphone' in name_lower and 'stereo mix' not in name_lower:
                print(f"   └─ ⭐ Likely your HEADPHONE MIC")
            elif 'stereo mix' in name_lower:
                print(f"   └─ ❌ This is STEREO MIX (internal audio) - AVOID")
    
    # Test top candidates
    print("\n" + "="*60)
    print("TESTING MICROPHONE DEVICES")
    print("="*60)
    print("\nI'll test the most likely devices.")
    print("Speak/tap into your headphone mic when prompted!")
    
    external_mics = []
    for device_id in input_devices:
        name = devices[device_id]['name'].lower()
        # Skip stereo mix, prioritize microphone/capture devices
        if 'stereo mix' not in name and ('microphone' in name or 'capture' in name):
            if test_specific_device(device_id):
                external_mics.append(device_id)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if external_mics:
        print(f"\n✅ Found {len(external_mics)} potential headphone microphone(s):")
        for mic_id in external_mics:
            print(f"   Device {mic_id}: {devices[mic_id]['name']}")
        
        best = external_mics[0]
        print(f"\n✅ RECOMMENDED: Use Device {best} for your voice recording")
        print(f"   ({devices[best]['name']})")
    else:
        print("\n❌ Could not identify headphone microphone")
        print("Troubleshooting:")
        print("   1. Check if headphone is properly plugged in")
        print("   2. Update audio drivers from your PC manufacturer")
        print("   3. Check Windows Settings > Sound > Input devices")
        print("   4. Disable Stereo Mix completely")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
