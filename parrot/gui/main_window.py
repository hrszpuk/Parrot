from PySide6.QtWidgets import *

from parrot.gui.widgets.chat_window import ChatWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parrot")
        self.setGeometry(600, 100, 1600, 900)  # Position and size (x, y, width, height)
        self.show()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        chat_window = ChatWindow()
        chat_window.add_message("Hello?", is_user=False)
        chat_window.add_message("Hello?", is_user=True)
        chat_window.add_message("Hello?", is_user=False)
        main_layout.addWidget(chat_window)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
