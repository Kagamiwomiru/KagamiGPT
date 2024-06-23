# アプリケーション設定画面
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QFormLayout
from PyQt5.QtCore import QSettings
from Helpers.DataKit import ConfigStore
from Helpers.DataKit.TextStore import AppSettingLabels


class ConfigShop(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadSettings()

    def initUI(self):
        self.setWindowTitle(AppSettingLabels.CS_WINDOW_TITLE.value)

        # Create layout and form fields
        layout = QVBoxLayout()
        formLayout = QFormLayout()
        
        self.openai_api_key_edit = QLineEdit()
        self.openai_api_key_edit.setMinimumWidth(ConfigStore.CS_TEXT_MINIMUM_SIZE)
        self.google_custom_search_api_key_edit = QLineEdit()
        self.google_custom_search_api_key_edit.setMinimumWidth(ConfigStore.CS_TEXT_MINIMUM_SIZE)
        self.google_custom_search_engine_id_edit = QLineEdit()
        self.google_custom_search_engine_id_edit.setMinimumWidth(ConfigStore.CS_TEXT_MINIMUM_SIZE)
        self.default_model_edit = QLineEdit()
        self.default_model_edit.setMinimumWidth(ConfigStore.CS_TEXT_MINIMUM_SIZE)
        self.config_file_path_label = QLabel(AppSettingLabels.CS_LABEL_CONFIGPATH.value)
        layout.addWidget(self.config_file_path_label)

        formLayout.addRow(QLabel(AppSettingLabels.CS_LABEL_OPENAPI_KEY.value), self.openai_api_key_edit)
        formLayout.addRow(QLabel(AppSettingLabels.CS_LABEL_GOOGLE_SEARCH_API_KEY.value), self.google_custom_search_api_key_edit)
        formLayout.addRow(QLabel(AppSettingLabels.CS_LABEL_GOOGLE_SEARCH_ENGINE_ID.value), self.google_custom_search_engine_id_edit)
        formLayout.addRow(QLabel(AppSettingLabels.CS_LABEL_DEFAULT_MODEL.value), self.default_model_edit)

        # Save Button
        save_button = QPushButton(AppSettingLabels.CS_LABEL_SAVE_BUTTON.value)
        save_button.clicked.connect(self.saveSettings)

        layout.addLayout(formLayout)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def loadSettings(self):
        settings = QSettings(ConfigStore.CONFIG_PATH, QSettings.IniFormat)
        self.config_file_path_label.setText(f'{AppSettingLabels.CS_LABEL_CONFIGPATH.value} {ConfigStore.CONFIG_PATH}')
        settings.beginGroup(ConfigStore.CS_GROUP)
        self.openai_api_key_edit.setText(settings.value(ConfigStore.CS_ITEM_OPENAPI_KEY, ''))
        self.google_custom_search_api_key_edit.setText(settings.value(ConfigStore.CS_ITEM_GOOGLE_SEARCH_API_KEY, ''))
        self.google_custom_search_engine_id_edit.setText(settings.value(ConfigStore.CS_ITEM_GOOGLE_SEARCH_ENGINE_ID, ''))
        self.default_model_edit.setText(settings.value(ConfigStore.CS_ITEM_DEFAULT_MODEL, ''))

    def saveSettings(self):
        settings = QSettings(ConfigStore.CONFIG_PATH, QSettings.IniFormat)
        settings.beginGroup(ConfigStore.CS_GROUP)
        settings.setValue(ConfigStore.CS_ITEM_OPENAPI_KEY, self.openai_api_key_edit.text())
        settings.setValue(ConfigStore.CS_ITEM_GOOGLE_SEARCH_API_KEY, self.google_custom_search_api_key_edit.text())
        settings.setValue(ConfigStore.CS_ITEM_GOOGLE_SEARCH_ENGINE_ID, self.google_custom_search_engine_id_edit.text())
        settings.setValue(ConfigStore.CS_ITEM_DEFAULT_MODEL, self.default_model_edit.text())

        settings.sync()  # Ensure settings are written to disk

