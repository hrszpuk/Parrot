from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout


class ChatBox(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Type a message...")

        send_button = QPushButton("Send")
        image_button = QPushButton("Insert Image")

        layout.addWidget(self.text_input)
        layout.addWidget(image_button)
        layout.addWidget(send_button)

        self.setLayout(layout)
