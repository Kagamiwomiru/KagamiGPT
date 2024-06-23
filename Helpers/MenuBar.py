#menu bar
from PyQt5.QtWidgets import QAction, QMenuBar, QMessageBox
from PyQt5.QtGui import QPixmap
from Helpers.DataKit import ConfigStore, ValueStore
from Helpers.DataKit.TextStore import MenuBarLabels
from Helpers.CharacterKit import CharacterEditerWindow
from Helpers.TokenCalculater import TokenCalcurater
from Helpers.ConfigShop import ConfigShop


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        # メニューバーを作成します。
        
        menu1 = self.addMenu(f'メニュー')

        # 「MyGPTについて」アクションを作成します。
        about_action = QAction(f'{ConfigStore.APP_NAME}について', self)
        about_action.triggered.connect(self.show_about_dialog)

        # 人格設定：カスタムの編集ウインドウ
        edit_custom_charactor = QAction(MenuBarLabels.MB_EDIT_CUSTOM_LABEL.value, self)
        edit_custom_charactor.triggered.connect(self.show_edit_custom_window)

        tool_tiktoken = QAction(MenuBarLabels.MB_TOOL_TIKTOKEN_LABEL.value, self)
        tool_tiktoken.triggered.connect(self.show_tool_tiktoken_window)

        # Config.iniの設定
        config_window = QAction(MenuBarLabels.MB_CONFIG_WINDOW_LABEL.value, self)
        config_window.triggered.connect(self.show_config_window)

        # メニュー項目に追加
        menu1.addAction(about_action)
        menu1.addAction(edit_custom_charactor)
        menu1.addAction(tool_tiktoken)
        menu1.addAction(config_window)


    def show_about_dialog(self):
        # 「MyGPTについて」ダイアログを表示します。
        about_text = f'''
        {ConfigStore.APP_NAME}
        バージョン： {ConfigStore.APP_VERSION}
        OpenAI APIバージョン: {ValueStore.openai_api_version}
        作者：{ConfigStore.APP_AUTHOR}
        '''
        about_dialog = QMessageBox(self)
        about_dialog.setWindowTitle(f'{ConfigStore.APP_NAME}について')
        about_dialog.setText(about_text)
        icon_pixmap = QPixmap(ConfigStore.APP_ICON)
        about_dialog.setIconPixmap(icon_pixmap)
        about_dialog.exec_()


    def show_edit_custom_window(self):
        # 人格設定を編集するウインドウを開きます。
        self.editer = CharacterEditerWindow()
        self.editer.show()


    def show_tool_tiktoken_window(self):
        '''
        トークン計算機
        '''

        self.token_calucater = TokenCalcurater()
        self.token_calucater.show()

    def show_config_window(self):
        '''
        アプリケーション設定
        '''

        self.config_shop = ConfigShop()
        self.config_shop.show()
