# AI Main function 
# 
from llama_cpp import Llama
from pathlib import Path

class AIModule:

    def __init__(self):
        current_file = Path(__file__).resolve()
        project_root = current_file.parent.parent.parent
        model_path = project_root / "models" / "mistral-7b-instruct-v0.2.Q4_K_M.gguf"

        print(f"Loading from model: {model_path}")



        self.model = Llama(
            model_path=str(model_path),
            n_ctx=2048,
            verbose=False,
        )
        print("Model load successfull")

    def ask(self, prompt: str) -> str:
        """Send prompt to model"""
        output = self.model(
            prompt, 
            max_tokens=100,
            temperature=0.7,
            top_p=0.9,)

        return output["choices"][0]["text"].strip()