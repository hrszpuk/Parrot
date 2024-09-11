from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class TopBar(QWidget):
    """Top bar widget."""

    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.layout = QVBoxLayout()

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        self.layout.addStretch()

        self.setLayout(self.layout)
