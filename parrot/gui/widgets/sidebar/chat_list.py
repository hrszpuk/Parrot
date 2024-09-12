from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListView, QListWidget, QVBoxLayout, QListWidgetItem, QWidget, QLabel, QPushButton


class ChatList(QWidget):
    chat_selected_signal = Signal(str)
    new_chat_button_pressed = Signal()

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Chats")
        self.layout.addWidget(self.title)

        self.new_chat_button = QPushButton("New Chat")
        self.new_chat_button.clicked.connect(self.new_chat_button_pressed)
        self.layout.addWidget(self.new_chat_button)

    def chat_button_pressed(self, model_name):
        """Return a slot that emits the model name when the button is clicked."""

        def slot():
            self.chat_selected_signal.emit(model_name)

        return slot

    def add_new_chat(self, model_name):
        button = QPushButton(model_name)
        button.clicked.connect(self.chat_button_pressed(model_name))
        self.layout.addWidget(button)
        self.layout.update()
