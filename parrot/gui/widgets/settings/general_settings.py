from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class GeneralSettings(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        label = QLabel("General Settings")
        self.layout.addWidget(label)
        self.setLayout(self.layout)
