from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from parrot.gui.widgets.chat_box import ChatBox
from parrot.gui.widgets.chat_message import ChatMessage
from parrot.gui.widgets.chat_message_list import ChatMessageList
from parrot.gui.widgets.top_bar import TopBar


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        chat_layout = QVBoxLayout()
        chat_widget = QWidget()
        chat_widget.setLayout(chat_layout)

        chat_top_bar = TopBar(title="Chat Name")
        chat_layout.addWidget(chat_top_bar)

        self.message_list = ChatMessageList()
        chat_layout.addWidget(self.message_list)

        chat_box = ChatBox()
        chat_box.message_sent.connect(self.add_message)

        chat_layout.addWidget(chat_box)

        layout.addWidget(chat_widget)

        self.setLayout(layout)

    def add_message(self, text, is_user=True, loading=False):
        message_widget = ChatMessage(text, is_user, loading)
        self.message_list.add_message(message_widget)
