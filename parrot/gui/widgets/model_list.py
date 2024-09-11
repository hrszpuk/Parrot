from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListView, QListWidget, QVBoxLayout, QWidget, QLabel, QListWidgetItem, QCheckBox, \
    QPushButton


class ModelList(QWidget):
    model_selected_signal = Signal(str, QPushButton)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.list = QListWidget()
        self.title = QLabel("Models")

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.list)

        models = ["Model 1", "Model 2", "Model 3"]
        for model in models:
            item = QListWidgetItem()
            button = QPushButton(model)
            button.clicked.connect(self.item_selected)
            self.list.addItem(item)
            self.list.setItemWidget(item, button)

    def item_selected(self):
        print(f"Selected: {self.sender().setVisible(False)}")
        pass
