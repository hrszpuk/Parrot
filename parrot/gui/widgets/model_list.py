from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListView, QListWidget, QVBoxLayout, QWidget, QLabel, QListWidgetItem, QCheckBox, \
    QPushButton


class ModelList(QWidget):
    model_selected_signal = Signal(str)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Models")
        self.layout.addWidget(self.title)

        models = ["Model 1", "Model 2", "Model 3"]
        for model in models:
            button = QPushButton(model)
            button.clicked.connect(self.model_button_pressed)
            self.layout.addWidget(button)

    def model_button_pressed(self, model_name):
        """Return a slot that emits the model name when the button is clicked."""

        def slot():
            self.model_selected_signal.emit(model_name)

        return slot
