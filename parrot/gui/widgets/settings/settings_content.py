from PySide6.QtWidgets import QStackedWidget

from parrot.gui.widgets.settings import AppearanceSettings
from parrot.gui.widgets.settings import ChatSettings
from parrot.gui.widgets.settings import GeneralSettings
from parrot.gui.widgets.settings import ModelSettings


class SettingsContent(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.general = GeneralSettings()
        self.appearance = AppearanceSettings()
        self.chats = ChatSettings()
        self.models = ModelSettings()

        self.addWidget(self.general)
        self.addWidget(self.appearance)
        self.addWidget(self.chats)
        self.addWidget(self.models)
