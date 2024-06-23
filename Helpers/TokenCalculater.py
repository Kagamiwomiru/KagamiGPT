# トークン計算機
from Helpers.GeneralKit import estimateToken
from Helpers.DataKit import ConfigStore
from Helpers.DataKit.TextStore import TokenCalculaterLabels
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QTextEdit, QWidget, QLabel


class TokenCalcurater(QWidget):
    '''
    トークン計算機
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TokenCalculaterLabels.TC_WINDOW_TITLE.value)
        self.setGeometry(300, 300, 300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.num_token = 0
        self.text_box = QTextEdit(self)
        self.text_box.setToolTip(TokenCalculaterLabels.TC_EDITER_INFO.value)
        self.button = QPushButton(TokenCalculaterLabels.TC_EDITER_BUTTON.value)
        self.token_lbl = QLabel(f"{TokenCalculaterLabels.TC_EDITER_LABEL.value}{self.num_token}")

        self.button.clicked.connect(self.calc_token)
        layout.addWidget(self.token_lbl)
        layout.addWidget(self.text_box)
        layout.addWidget(self.button)

    def calc_token(self):
        self.num_token = estimateToken(ConfigStore.OPENAI_MODEL, self.text_box.toPlainText())
        self.token_lbl.setText(f"{TokenCalculaterLabels.TC_EDITER_LABEL.value}{self.num_token}")
