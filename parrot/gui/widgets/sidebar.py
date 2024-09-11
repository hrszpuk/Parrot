from PySide6.QtWidgets import QWidget, QVBoxLayout

from parrot.gui.widgets.bottom_bar import BottomBar
from parrot.gui.widgets.top_bar import TopBar


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        top = TopBar(title="Parrot")
        self.layout.addWidget(top)

        bottom = BottomBar()
        self.layout.addWidget(bottom)
