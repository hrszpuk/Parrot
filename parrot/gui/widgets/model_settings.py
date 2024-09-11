from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ModelSettings(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        label = QLabel("Model Settings")
        self.layout.addWidget(label)
