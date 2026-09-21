import sounddevice as sd
import numpy as np

def select_mic(name_hint="Microphone Array", driver_hint="WASAPI"):
    """
    Finds and sets the input device matching the name/driver hints.
    Falls back to the system default if no match is found.
    """
    devices = sd.query_devices()
    hostapis = sd.query_hostapis()

    for i, d in enumerate(devices):
        if d['max_input_channels'] > 0:
            hostapi_name = hostapis[d['hostapi']]['name']
            if name_hint in d['name'] and driver_hint in hostapi_name:
                sd.default.device = (i, None)  # (input, output)
                print(f"Selected mic: [{i}] {d['name']} ({hostapi_name})")
                return i

    print("No matching mic found — using system default input device.")
    return None


def amplify(audio, factor=3.0):
    """Boosts audio volume by a multiplier, clipping to avoid distortion."""
    amplified = audio * factor
    return np.clip(amplified, -1.0, 1.0)