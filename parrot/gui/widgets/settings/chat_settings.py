from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ChatSettings(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        label = QLabel("Chat Settings")
        self.layout.addWidget(label)
        self.setLayout(self.layout)
