from PySide6.QtWidgets import *

from parrot.gui.widgets.chat import ChatWindow
from parrot.gui.widgets.my_copilots import ModelMenu
from parrot.gui.widgets.settings import SettingsMenu
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
        self.sidebar_widget.bottom.ai_model_manager_clicked.connect(self.open_copilots_menu)

        self.chat_window = ChatWindow()
        self.chat_window.add_message("Hello?", is_user=False)
        self.chat_window.add_message("Hello?", is_user=True)
        self.chat_window.add_message("Hello?", is_user=False)
        self.main_layout.addWidget(self.chat_window)

        self.settings_menu = SettingsMenu()
        self.settings_menu.settings_closed.connect(self.show_main_content)
        self.settings_menu.setVisible(False)
        self.main_layout.addWidget(self.settings_menu)

        self.copilots_menu = ModelMenu()
        self.copilots_menu.my_copilots_closed.connect(self.show_main_content)
        self.copilots_menu.setVisible(False)
        self.main_layout.addWidget(self.copilots_menu)

        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.setCentralWidget(widget)

    def open_settings_menu(self):
        self.chat_window.setVisible(False)
        self.sidebar_widget.setVisible(False)

        self.settings_menu.setVisible(True)

    def open_copilots_menu(self):
        self.chat_window.setVisible(False)
        self.sidebar_widget.setVisible(False)

        self.copilots_menu.setVisible(True)

    def show_main_content(self):
        self.settings_menu.setVisible(False)
        self.copilots_menu.setVisible(False)
        self.chat_window.setVisible(True)
        self.sidebar_widget.setVisible(True)
