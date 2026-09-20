import sounddevice as sd
import soundfile as sf
import subprocess
import ollama
from faster_whisper import WhisperModel

# Load STT model once (slow to load, fast to reuse)
print("Loading whisper model stay patient, nigga👍...")
stt_model = WhisperModel("base", device="cpu", compute_type="int8")

def record_audio(filename="input.wav", duration=5, samplerate=16000):
    print(f"Recording for {duration} seconds... speak now niggaaa.")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)
    print("Recording saved.")

def transcribe(filename="input.wav"):
    segments, _ = stt_model.transcribe(filename)
    text = " ".join(segment.text for segment in segments).strip()
    return text

def ask_ollama(prompt, model="qwen2.5-coder:1.5b"):
    response = ollama.chat(model=model, messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]

def speak(text, output_file="response.wav"):
    subprocess.run(
        ["python", "-m", "piper",
         "--model", "en_US-lessac-medium.onnx",
         "--output_file", output_file],
        input=text.encode(),
    )
    # Play it back
    data, samplerate = sf.read(output_file)
    sd.play(data, samplerate)
    sd.wait()

# Main loop
while True:
    input("\nPress Enter to talk (or Ctrl+C to quit)...")
    record_audio()
    user_text = transcribe()
    print(f"You said: {user_text}")

    if not user_text:
        print("Didn't catch that, try again.")
        continue

    reply = ask_ollama(user_text)
    print(f"Assistant: {reply}")

    speak(reply)