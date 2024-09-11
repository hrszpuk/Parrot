from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListView, QListWidget, QVBoxLayout, QListWidgetItem, QWidget, QLabel, QPushButton


class ChatList(QWidget):
    chat_selected_signal = Signal(str)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Chats")
        self.layout.addWidget(self.title)

        models = ["Chat 1", "Chat 2", "Chat 3"]
        for model in models:
            button = QPushButton(model)
            button.clicked.connect(self.chat_button_pressed)
            self.layout.addWidget(button)

    def chat_button_pressed(self, model_name):
        """Return a slot that emits the model name when the button is clicked."""

        def slot():
            self.chat_selected_signal.emit(model_name)

        return slot
