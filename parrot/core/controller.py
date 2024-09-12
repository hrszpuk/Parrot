from .chat_manager import ChatManager


class Controller:
    """Handles business logic for the application and acts as the interface between the GUI and the ChatManager."""

    def __init__(self):
        self.chat_manager = ChatManager()
        self.current_chat_id = None

    def start_new_chat(self, chat_name, model_name="default_model"):
        self.current_chat_id = self.chat_manager.create_chat_session(chat_name, model_name)
        return self.current_chat_id

    def set_current_chat(self, chat_id):
        self.current_chat_id = chat_id

    def get_chat_sessions(self):
        return self.chat_manager.get_chat_sessions()

    def get_current_chat_history(self):
        if self.current_chat_id is None:
            return []

        return self.chat_manager.get_messages(self.current_chat_id)

    def add_message_to_current_chat(self, sender, message):
        if self.current_chat_id is None:
            raise ValueError("No current chat session set.")

        self.chat_manager.add_message(self.current_chat_id, sender, message)

    def close(self):
        self.chat_manager.close()
