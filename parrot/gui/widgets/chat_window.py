from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from parrot.gui.widgets.chat_box import ChatBox
from parrot.gui.widgets.chat_message import ChatMessage
from parrot.gui.widgets.chat_message_list import ChatMessageList


# The rest of your code remains unchanged
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.top_bar = ChatWindow.create_top_bar(chat_name="Conversation Name")
        layout.addWidget(self.top_bar)

        self.message_list = ChatMessageList()
        layout.addWidget(self.message_list)

        self.chat_box = ChatBox()
        self.chat_box.message_sent.connect(self.add_message)

        layout.addWidget(self.chat_box)

        self.setLayout(layout)

    def add_message(self, text, is_user=True, loading=False):
        message_widget = ChatMessage(text, is_user, loading)
        self.message_list.add_message(message_widget)

    @staticmethod
    def create_top_bar(chat_name):
        """Creates a top bar widget with a title label."""
        top_bar = QWidget()
        layout = QVBoxLayout()

        title_label = QLabel(chat_name)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label)

        layout.addStretch()
        top_bar.setLayout(layout)
        return top_bar
