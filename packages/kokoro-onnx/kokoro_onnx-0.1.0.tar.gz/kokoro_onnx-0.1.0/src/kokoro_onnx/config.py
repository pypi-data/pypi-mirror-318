from pathlib import Path
import json
from functools import lru_cache

class KoKoroConfig:
    def __init__(self, model_path: str, voices_path: str):
        self.model_path = model_path
        self.voices_path = voices_path
    
    def validate(self):
        if not Path(self.voices_path).exists():
            error_msg = f"Voices file not found at {self.voices_path}"
            error_msg += "\nYou can download the voices file using the following command:"
            error_msg += "\nwget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json"
            raise FileNotFoundError(error_msg)
            
        if not Path(self.model_path).exists():
            error_msg = f"Model file not found at {self.model_path}"
            error_msg += "\nYou can download the model file using the following command:"
            error_msg += "\nwget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx"
            raise FileNotFoundError(error_msg)
    
    @lru_cache
    def get_voice_names(self):
        with open(self.voices_path) as f:
            voices = json.load(f)
        return voices.keys()