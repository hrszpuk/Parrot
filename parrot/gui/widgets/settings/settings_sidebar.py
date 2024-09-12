from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class SettingsSidebar(QWidget):
    category_selected = Signal(int)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        categories = ["General", "Appearance", "Chats", "Models"]
        for index, category in enumerate(categories):
            button = QPushButton(category)
            button.clicked.connect(lambda _, i=index: self.category_selected.emit(i))
            self.layout.addWidget(button)
