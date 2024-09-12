from PySide6.QtWidgets import QWidget, QVBoxLayout

from .bottom_bar import BottomBar
from .chat_list import ChatList
from .model_list import ModelList
from parrot.gui.widgets.top_bar import TopBar


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.top = TopBar(title="Parrot")
        self.layout.addWidget(self.top)

        # model_list = (ModelList())
        # self.layout.addWidget(model_list)

        self.chat_list = ChatList()
        self.layout.addWidget(self.chat_list)

        self.layout.addStretch()

        self.bottom = BottomBar()
        self.layout.addWidget(self.bottom)
