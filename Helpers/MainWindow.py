# Mainウインドウ
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from PyQt5.QtGui import QIcon
from Helpers.TabKit.NormalChatTab import NormalChatTab
from Helpers.TabKit.CompactChatTab import CompactChatTab
# from Helpers.TabKit.PDFChatTab import PDFChatTab
from Helpers.MenuBar import MenuBar
from Helpers.DataKit import ConfigStore
from Helpers.DataKit.TextStore import MainWindowLabels
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(ConfigStore.APP_NAME)
        self.setWindowIcon(QIcon(ConfigStore.APP_ICON))

        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        self.setGeometry(0, 0,ConfigStore.MAIN_WIN_WIDTH, ConfigStore.MAIN_WIN_HEIGHT)
        self.tab0 = CompactChatTab()
        self.tab1 = NormalChatTab()
        # self.tab2 = PDFChatTab()

        self.tabWidget.addTab(self.tab0, MainWindowLabels.MAIN_WIN_TAB0.value)
        self.tabWidget.addTab(self.tab1, MainWindowLabels.MAIN_WIN_TAB1.value)
        # self.tabWidget.addTab(self.tab2, MainWindowLabels.MAIN_WIN_TAB2.value)

        # タブ切り替えイベント
        self.tabWidget.currentChanged.connect(self.changeWindowSize)
        

        self.setMenuBar(MenuBar())


    def changeWindowSize(self, index):
        '''
        タブによってウインドウサイズを変更する
        '''
        if index == 0:
            self.resize(ConfigStore.TAB_ZERO_WIDTH, ConfigStore.TAB_ZERO_HEIGHT)
        elif index == 1:
            self.resize(ConfigStore.TAB_ONE_WIDTH, ConfigStore.TAB_ONE_HEIGHT)
        elif index == 2:
            self.resize(ConfigStore.TAB_ONE_WIDTH, ConfigStore.TAB_ONE_HEIGHT)

        
