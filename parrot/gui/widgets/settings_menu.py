from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, Signal

from parrot.gui.widgets.settings_content import SettingsContent
from parrot.gui.widgets.settings_sidebar import SettingsSidebar


class SettingsMenu(QWidget):
    """A fullscreen settings menu widget. This widget contains all the settings for the application."""
    settings_closed = Signal()

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        title = QLabel("Settings")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(title)

        self.layout.addStretch()

        self.internal_layout = QHBoxLayout()

        self.sidebar = SettingsSidebar()
        self.sidebar.category_selected.connect(self.switch_page)
        self.internal_layout.addWidget(self.sidebar)

        self.content = SettingsContent()
        self.internal_layout.addWidget(self.content)

        self.layout.addLayout(self.internal_layout)

        self.layout.addStretch()

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.settings_closed.emit)
        self.layout.addWidget(close_button)

        self.setLayout(self.layout)

    def switch_page(self, index):
        self.content.setCurrentIndex(index)
