import shutil
from huggingface_hub import hf_hub_download

onnx_path = hf_hub_download(
    repo_id="rhasspy/piper-voices",
    filename="en/en_US/lessac/medium/en_US-lessac-medium.onnx"
)
json_path = hf_hub_download(
    repo_id="rhasspy/piper-voices",
    filename="en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"
)

shutil.copy(onnx_path, "en_US-lessac-medium.onnx")
shutil.copy(json_path, "en_US-lessac-medium.onnx.json")

print("Done — voice files copied into this folder.")