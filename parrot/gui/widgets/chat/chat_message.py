from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QAbstractItemView, QLabel, QHBoxLayout, QWidget


class ChatMessage(QWidget):
    """
    A widget that displays a single message in a chat-like interface.
    This widget is used by the ChatBox widget to display messages.
    """

    def __init__(self, text, is_user=True, loading=False):
        super().__init__()
        self.text = text
        self.is_user = is_user
        self.loading = loading

        layout = QHBoxLayout()

        icon = QLabel()
        icon.setFixedSize(30, 30)
        icon.setStyleSheet("background-color: #f0f0f0; border-radius: 15px;")

        message_label = QLabel(self.text)
        message_label.setWordWrap(True)
        message_label.setTextFormat(Qt.TextFormat.MarkdownText)

        if self.is_user:
            layout.addStretch()  # Push to the right for user messages
            layout.addWidget(message_label)
            layout.addWidget(icon)
        else:
            layout.addWidget(icon)
            layout.addWidget(message_label)
            layout.addStretch()  # Push to the left for other messages

        if self.loading:
            # Add a placeholder for a loading indicator (optional)
            loading_label = QLabel("...")  # Replace with an actual spinner/loading icon if needed
            layout.addWidget(loading_label)

        self.setLayout(layout)
