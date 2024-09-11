from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class BottomBar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        settings_button = QPushButton("Settings")
        self.layout.addWidget(settings_button)

        theme_button = QPushButton("Light/Dark Mode")
        self.layout.addWidget(theme_button)

        search_button = QPushButton("Search")
        self.layout.addWidget(search_button)

        self.setLayout(self.layout)
