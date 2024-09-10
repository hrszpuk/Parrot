from PySide6.QtWidgets import QListView, QScrollArea, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


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
        self.messages_layout.addStretch()
        self.messages_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
