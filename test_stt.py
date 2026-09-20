from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")

segments, info = model.transcribe("test.wav")

print(f"Detected language: {info.language}")
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")