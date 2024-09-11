from PySide6.QtWidgets import QWidget, QVBoxLayout

from parrot.gui.widgets.bottom_bar import BottomBar
from parrot.gui.widgets.chat_list import ChatList
from parrot.gui.widgets.model_list import ModelList
from parrot.gui.widgets.top_bar import TopBar


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        top = TopBar(title="Parrot")
        self.layout.addWidget(top)

        model_list = (ModelList())
        self.layout.addWidget(model_list)

        chat_list = ChatList()
        self.layout.addWidget(chat_list)

        bottom = BottomBar()
        self.layout.addWidget(bottom)
