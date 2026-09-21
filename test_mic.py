import sounddevice as sd
import soundfile as sf
import numpy as np
from mic_utils import select_mic, amplify

select_mic()

print("Recording 5 seconds... SPEAK NOW")
audio = sd.rec(int(5 * 16000), samplerate=16000, channels=1)
sd.wait()

audio = amplify(audio, factor=3.0)

sf.write("mic_test.wav", audio, 16000)
print("Saved mic_test.wav")
print("Max amplitude:", np.abs(audio).max())