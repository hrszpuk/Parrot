from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class BottomBar(QWidget):
    settings_clicked = Signal()
    theme_clicked = Signal()
    ai_model_manager_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        settings_button = QPushButton("Settings")
        settings_button.clicked.connect(self.settings_clicked.emit)
        self.layout.addWidget(settings_button)

        theme_button = QPushButton("Light/Dark Mode")
        theme_button.clicked.connect(self.theme_clicked.emit)
        self.layout.addWidget(theme_button)

        ai_model_manager_button = QPushButton("My Chatbots")
        ai_model_manager_button.clicked.connect(self.ai_model_manager_clicked.emit)
        self.layout.addWidget(ai_model_manager_button)

        self.setLayout(self.layout)
