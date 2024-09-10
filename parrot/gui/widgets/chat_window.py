from PySide6.QtWidgets import QWidget, QVBoxLayout

from parrot.gui.widgets.chat_box import ChatBox
from parrot.gui.widgets.chat_message import ChatMessage
from parrot.gui.widgets.chat_message_list import ChatMessageList


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the message list
        self.message_list = ChatMessageList()
        layout.addWidget(self.message_list)

        # Create the input box
        self.chat_box = ChatBox()
        layout.addWidget(self.chat_box)

        self.setLayout(layout)

    def add_message(self, text, is_user=True, loading=False):
        message_widget = ChatMessage(text, is_user, loading)
        self.message_list.add_message(message_widget)
