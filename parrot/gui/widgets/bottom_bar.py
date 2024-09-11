from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class BottomBar(QWidget):
    settings_clicked = Signal()
    theme_clicked = Signal()
    search_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        settings_button = QPushButton("Settings")
        settings_button.clicked.connect(self.settings_clicked.emit)
        self.layout.addWidget(settings_button)

        theme_button = QPushButton("Light/Dark Mode")
        theme_button.clicked.connect(self.theme_clicked.emit)
        self.layout.addWidget(theme_button)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_clicked.emit)
        self.layout.addWidget(search_button)

        self.setLayout(self.layout)
