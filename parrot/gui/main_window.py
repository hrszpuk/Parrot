from datetime import datetime

from PySide6.QtWidgets import *

from parrot.core import Controller
from parrot.gui.widgets.chat import ChatWindow
from parrot.gui.widgets.my_copilots import ModelMenu
from parrot.gui.widgets.settings import SettingsMenu
from parrot.gui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.controller = Controller()

        self.setWindowTitle("Parrot")
        self.setGeometry(600, 100, 1400, 800)
        self.show()

        self.main_layout = QHBoxLayout()

        self.sidebar_widget = Sidebar()
        self.main_layout.addWidget(self.sidebar_widget)

        self.sidebar_widget.chat_list.new_chat_button_pressed.connect(self.create_new_chat)
        self.sidebar_widget.bottom.settings_clicked.connect(self.open_settings_menu)
        self.sidebar_widget.bottom.ai_model_manager_clicked.connect(self.open_copilots_menu)

        self.chat_window = ChatWindow()
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

    def create_new_chat(self):
        chat_name = f"New Chat ({len(self.controller.get_chat_sessions())})"
        self.sidebar_widget.chat_list.add_new_chat(chat_name)

        self.controller.start_new_chat(chat_name)

        self.chat_window.chat_top_bar.title = chat_name
        self.chat_window.message_list.clear_messages()
        self.chat_window.chat_box.text_input.setText("")

    def send_message(self):
        message = self.chat_window.chat_box.get_text()

        self.controller.add_message_to_current_chat("user", message)
        self.chat_window.add_message(message, is_user=True, loading=False)
        self.chat_window.chat_box.clear_text()

    def load_chat_history(self, chat_id):
        self.controller.set_current_chat(chat_id)

        chat_history = self.controller.get_current_chat_history()

        self.chat_window.message_list.clear_messages()
        for message in chat_history:
            self.chat_window.message_list.add_message(message[1], message[2])  # (sender, message)

    def closeEvent(self, event):
        self.controller.close()
        event.accept()

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
