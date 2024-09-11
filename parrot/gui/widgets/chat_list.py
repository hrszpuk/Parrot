from PySide6.QtWidgets import QListView, QListWidget, QVBoxLayout, QListWidgetItem, QWidget, QLabel


class ChatList(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Chats")
        self.list = QListWidget()

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.list)
