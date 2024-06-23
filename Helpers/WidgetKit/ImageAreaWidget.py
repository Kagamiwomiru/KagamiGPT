from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from Helpers.DataKit import ValueStore
from Helpers.DataKit.TextStore import ImageAreaLabels

class ImageAreaWidget(QWidget):
    '''
    画像の入力管理
    '''
    def __init__(self, console, parent=None):
            super(ImageAreaWidget, self).__init__(parent)
            self.console = console
            self.setAcceptDrops(True)

            # ウィジェットの実装
            self.label = QLabel(ImageAreaLabels.IA_LABEL.value)
            self.label.setAlignment(Qt.AlignCenter)
            self.remove_button = QPushButton(ImageAreaLabels.IA_REMOVE_BUTTON.value)
            self.remove_button.clicked.connect(self.removeImg)
            

            # レイアウト設定
            layout = QVBoxLayout()
            self.setLayout(layout)

            # ウィジェットを配置
            layout.addWidget(self.label)
            layout.addWidget(self.remove_button)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            ValueStore.image_filepath = url.toLocalFile()
            self.load_image(ValueStore.image_filepath)
            self.console.outputText(ValueStore.image_filepath)

    def load_image(self, path):
        pixmap = pg.QtGui.QPixmap(path)
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)

    def removeImg(self):
         '''
         画像を削除
         '''
         self.label.clear()
         self.label.setText(ImageAreaLabels.IA_LABEL.value)
         ValueStore.image_filepath = ""