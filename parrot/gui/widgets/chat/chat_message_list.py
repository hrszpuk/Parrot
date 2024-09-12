from PySide6.QtWidgets import QListView, QScrollArea, QWidget, QVBoxLayout, QSizePolicy, QLabel
from PySide6.QtCore import Qt

from parrot.gui.widgets.chat import ChatMessage


class ChatMessageList(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setVisible(True)
        self.setWidgetResizable(True)

        self.messages_widget = QWidget()
        self.messages_layout = QVBoxLayout()

        self.messages_widget.setLayout(self.messages_layout)
        self.setWidget(self.messages_widget)

    def add_message(self, message_widget):
        self.messages_layout.addWidget(message_widget)
        self.messages_widget.adjustSize()
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def clear_messages(self):
        for i in reversed(range(self.messages_layout.count())):
            self.messages_layout.itemAt(i).widget().deleteLater()
        self.messages_widget.adjustSize()
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
