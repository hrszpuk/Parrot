from PySide6.QtWidgets import *

from parrot.gui.widgets.chat_window import ChatWindow
from parrot.gui.widgets.settings_menu import SettingsMenu
from parrot.gui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parrot")
        self.setGeometry(600, 100, 1400, 800)
        self.show()

        self.main_layout = QHBoxLayout()

        self.sidebar_widget = Sidebar()
        self.main_layout.addWidget(self.sidebar_widget)

        self.sidebar_widget.bottom.settings_clicked.connect(self.open_settings_menu)

        self.chat_window = ChatWindow()
        self.chat_window.add_message("Hello?", is_user=False)
        self.chat_window.add_message("Hello?", is_user=True)
        self.chat_window.add_message("Hello?", is_user=False)
        self.main_layout.addWidget(self.chat_window)

        self.settings_menu = SettingsMenu()
        self.settings_menu.settings_closed.connect(self.show_main_content)
        self.settings_menu.setVisible(False)

        self.main_layout.addWidget(self.settings_menu)

        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.setCentralWidget(widget)

    def open_settings_menu(self):
        self.chat_window.setVisible(False)
        self.sidebar_widget.setVisible(False)

        self.settings_menu.setVisible(True)

    def show_main_content(self):
        self.settings_menu.setVisible(False)
        self.chat_window.setVisible(True)
        self.sidebar_widget.setVisible(True)
