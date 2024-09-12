import os
import shutil
from transformers import AutoModel, AutoTokenizer


class ModelManager:
    """Manages installing new open-source models, keeping track of installed models, and loading models onto the CPU/GPU."""

    def __init__(self, models_dir='models'):
        self.models_dir = models_dir
        os.makedirs(self.models_dir, exist_ok=True)  # Ensure models directory exists

    def download_model(self, model_name: str):
        """Downloads the specified model from Hugging Face and saves it locally."""
        model_path = os.path.join(self.models_dir, model_name)
        if not os.path.exists(model_path):
            print(f"Downloading model: {model_name}")
            AutoModel.from_pretrained(model_name).save_pretrained(model_path)
            AutoTokenizer.from_pretrained(model_name).save_pretrained(model_path)
        else:
            print(f"Model {model_name} is already downloaded.")

    def load_model(self, model_name: str):
        """Loads the specified model from disk to CPU/GPU."""
        model_path = os.path.join(self.models_dir, model_name)
        if os.path.exists(model_path):
            print(f"Loading model: {model_name}")
            model = AutoModel.from_pretrained(model_path)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            return model, tokenizer
        else:
            raise FileNotFoundError(f"Model {model_name} not found. Please download it first.")

    def delete_model(self, model_name: str):
        """Deletes the specified model from disk."""
        model_path = os.path.join(self.models_dir, model_name)
        if os.path.exists(model_path):
            shutil.rmtree(model_path)
            print(f"Deleted model: {model_name}")
        else:
            print(f"Model {model_name} not found.")

    def list_models(self):
        """Lists all installed models."""
        return os.listdir(self.models_dir)
