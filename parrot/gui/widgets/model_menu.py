from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, Signal


class ModelMenu(QWidget):
    """A fullscreen model menu widget. This widget contains all the model settings for the application."""
    my_copilots_closed = Signal()

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        title = QLabel("Model Manager")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(title)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.my_copilots_closed.emit)
        self.layout.addWidget(close_button)

        self.setLayout(self.layout)
