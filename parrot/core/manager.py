class ModelManager:
    """Manages installing new open-source models, keeping track of installed models, and loading model onto the CPU/GPU."""

    def __init__(self):
        pass

    def download_model(self, model_name: str):
        """Downloads the specified model from the internet."""
        pass

    def load_model(self, model_name: str):
        """Loads the specified model onto the CPU/GPU."""
        pass

    def delete_model(self, model_name: str):
        """Deletes the specified model from the disk."""
        pass

    def list_models(self):
        """Lists all installed models."""
        pass
