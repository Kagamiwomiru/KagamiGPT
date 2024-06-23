# Tabの基底クラス
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from pyqtgraph.dockarea import Dock, DockArea


class BaseTab(QWidget):
    def __init__(self):
        super().__init__()
        self.area = DockArea()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.area)

    def addWidget(self, widget, dock_label="", size=(None, None), hide_label=True):
        '''
        dockにウィジェットを追加する
        
        usage:
            dummy_widget = self.addWidget(dock_label, size=(1, 10))
        
        Parameters
        ---
        widget  :   Qt.widget
            Qtウィジェットオブジェクト
        
        dock_label  :   str
            dock名
        
        size    :   taple
            width, heightのサイズ

        hide_label=True  :   bool
            dockのラベルを非表示にする
        '''


        widget_dock = Dock(dock_label, size=size)
        widget_dock.addWidget(widget)
        if hide_label:
            widget_dock.hideTitleBar()

        return widget_dock