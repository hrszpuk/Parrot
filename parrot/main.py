import sys
from parrot.gui import *
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

    # Unload models

    sys.exit(0)
