"""
Audio Recording Test Script
Tests microphone input and audio recording with your headphone setup
"""

import sounddevice as sd
import numpy as np
import wave
from datetime import datetime

def list_audio_devices():
    """List all available audio devices"""
    print("=" * 60)
    print("Available Audio Devices")
    print("=" * 60)
    devices = sd.query_devices()
    microphone_devices = []
    
    for i, device in enumerate(devices):
        print(f"{i}: {device['name']}")
        print(f"   Channels (In/Out): {device['max_input_channels']}/{device['max_output_channels']}")
        if device['max_input_channels'] > 0:
            print(f"   ✓ Can record from this device")
            # Identify microphone devices (not stereo mix)
            if 'microphone' in device['name'].lower() or 'capture' in device['name'].lower():
                microphone_devices.append(i)
        print()
    
    return microphone_devices

def test_recording(duration=5, device=None, sample_rate=44100):
    """Record audio and save to file"""
    print(f"\nRecording for {duration} seconds...")
    print("Speak into your headphone microphone now!")
    print("-" * 40)
    
    try:
        # Record audio
        recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, 
                          channels=2, device=device, dtype='float32')
        sd.wait()
        print("Recording complete!")
        
        # Save recording
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"voice_test_{timestamp}.wav"
        
        # Convert to 16-bit PCM
        recording_int16 = (recording * 32767).astype('int16')
        
        with wave.open(filename, 'wb') as wav_file:
            wav_file.setnchannels(2)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(recording_int16.tobytes())
        
        print(f"✓ Recording saved as: {filename}")
        
        # Check audio levels
        max_level = np.max(np.abs(recording))
        print(f"Peak audio level: {max_level:.3f} (0.0-1.0 scale)")
        
        if max_level < 0.05:
            print("⚠ WARNING: Audio level is very low - adjust microphone volume")
        elif max_level > 0.95:
            print("⚠ WARNING: Audio level is too high - reduce microphone volume to avoid distortion")
        else:
            print("✓ Audio level looks good!")
            
    except Exception as e:
        print(f"❌ Error during recording: {e}")
        print("Make sure you have 'sounddevice' installed: pip install sounddevice")

def main():
    print("\n" + "=" * 60)
    print("HEADPHONE AUDIO SETUP TEST")
    print("=" * 60)
    
    # List devices and get microphone suggestions
    microphone_devices = list_audio_devices()
    
    print("\n" + "=" * 60)
    print("MICROPHONE SELECTION GUIDE")
    print("=" * 60)
    print("❌ AVOID: Stereo Mix devices (they record internal/system audio)")
    print("✅ CHOOSE: Microphone or Capture devices")
    print()
    
    if microphone_devices:
        print("Recommended microphone devices:")
        for i, dev_id in enumerate(microphone_devices):
            device = sd.query_devices()[dev_id]
            print(f"  {i+1}. Device {dev_id}: {device['name']}")
        print()
        
        # Auto-select the best microphone
        selected_device = microphone_devices[0]  # Use first microphone
        device_name = sd.query_devices()[selected_device]['name']
        print(f"✓ Auto-selected: Device {selected_device} - {device_name}")
        print("   (This should be your headphone microphone)")
        
        # Test recording with auto-selected device
        print("\n" + "=" * 60)
        print("TESTING MICROPHONE RECORDING")
        print("=" * 60)
        
        test_recording(duration=5, device=selected_device)
        
    else:
        print("❌ No microphone devices found!")
        print("   Make sure your headphone microphone is properly connected.")
        return
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)
    print("✓ Check the generated WAV file to verify audio quality")
    print("✓ Play it back to confirm your headphone microphone works properly")
    print("✓ If you still hear only internal audio, try a different microphone device")

if __name__ == "__main__":
    main()
