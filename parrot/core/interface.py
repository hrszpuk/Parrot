import json
from datetime import datetime


class ModelInterface:
    """For interfacing with the model and logging queries/responses."""

    def __init__(self, model, tokenizer, log_file='chat_log.json'):
        self.model = model
        self.tokenizer = tokenizer
        self.log_file = log_file
        self.chat_history = []

    def generate(self, input_text: str):
        """Generates output based on the input text using the loaded model and logs the interaction."""

        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model(**inputs)

        ai_output = "AI response based on model output"
        self.log_interaction(input_text, ai_output)

        return ai_output

    def log_interaction(self, user_input: str, ai_output: str):
        """Logs the interaction between user input and AI output."""

        entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "ai_output": ai_output
        }

        self.chat_history.append(entry)

        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def get_chat_history(self):
        """Returns the logged chat history."""
        return self.chat_history
