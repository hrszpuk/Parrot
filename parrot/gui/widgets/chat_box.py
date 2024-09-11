from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout


class ChatBox(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Type a message...")

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_button_clicked)

        layout.addWidget(self.text_input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_button_clicked(self):
        self.text_input.clear()
