from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class ConsoleWidget(QWidget):
    def __init__(self, parent=None):
        super(ConsoleWidget, self).__init__(parent)
        
        self.layout = QVBoxLayout(self)
        
        # self.output_text = StreamQText()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        
        self.layout.addWidget(self.output_text)
        
    def outputText(self, text):
        '''
        コンソールにログを出力します。
        '''

        self.output_text.append(text)
