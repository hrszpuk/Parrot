from huggingface_hub import HfApi


class ModelExplorerFinder:
    """Handles both exploring popular models and searching for specific models on Hugging Face."""

    def __init__(self):
        self.api = HfApi()

    def get_popular_models(self, limit=10):
        """Returns a list of popular models from Hugging Face."""
        popular_models = self.api.list_models(sort='downloads', limit=limit)
        model_names = [model.id for model in popular_models]
        return model_names

    def search_model(self, query: str, limit=10):
        """Searches Hugging Face models based on a query."""
        search_results = self.api.list_models(search=query, limit=limit)
        model_names = [model.id for model in search_results]
        return model_names
