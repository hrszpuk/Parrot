from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from parrot.gui.widgets.chat import ChatBox
from parrot.gui.widgets.chat import ChatMessage
from parrot.gui.widgets.chat import ChatMessageList
from parrot.gui.widgets.top_bar import TopBar


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.chat_layout = QVBoxLayout()
        self.chat_widget = QWidget()
        self.chat_widget.setLayout(self.chat_layout)

        self.chat_top_bar = TopBar(title="Chat Name")
        self.chat_layout.addWidget(self.chat_top_bar)

        self.message_list = ChatMessageList()
        self.chat_layout.addWidget(self.message_list)

        self.chat_box = ChatBox()
        self.chat_box.message_sent.connect(self.add_message)

        self.chat_layout.addWidget(self.chat_box)

        self.layout.addWidget(self.chat_widget)

        self.setLayout(self.layout)

    def add_message(self, text, is_user=True, loading=False):
        message_widget = ChatMessage(text, is_user, loading)
        self.message_list.add_message(message_widget)
