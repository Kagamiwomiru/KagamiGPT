from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QLineEdit
from Helpers.DataKit import ConfigStore, ValueStore
import markdown
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Helpers.GeneralKit import  StreamQText
from PyQt5.QtCore import QUrl, Qt


class ChatWidget(QWidget):
    '''
    AIとのやりとりを表示します。
    Markdown記法をサポートします。
    '''
    def __init__(self, console):
        super().__init__()
        self.console = console
        # 処理の定義
        ## QWebEngineViewを初期化
        self.browser = QWebEngineView()
        self.render_markdown(ValueStore.markdown_text)
        # 速報版を出す
        self.preview_text = StreamQText()
        self.preview_text.setStyleSheet(ConfigStore.RESPONSE_BOARD_STYLE_SHEET)  
        self.preview_text.setReadOnly(True)
        
        # PreviousPrompt
        self.previous_prompt_area = QLineEdit()
        self.previous_prompt_area.setReadOnly(True)
        self.previous_prompt_area.setStyleSheet(ConfigStore.PREVIOUS_PROMPT_STYLE_SHEET)
        self.previous_prompt_area.setAlignment(Qt.AlignRight)

        # レイアウトの定義        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.preview_text)
        self.layout.addWidget(self.previous_prompt_area)

        # レイアウトをセット
        self.setLayout(self.layout)
        # self.preview_text.hide()


    def compileText(self, text):
        '''
        ウインドウにテキストを整形して出力します。
        '''
        ValueStore.markdown_text = text
        self.render_markdown(ValueStore.markdown_text)

    def render_markdown(self, markdown_text):
        '''
        markdown記法をHTMLにレンダリングします。        
        '''
        ## MarkdownをHTMLに変換
        html_text = markdown.markdown(text=markdown_text, extensions=['fenced_code'])
        highlight_js_path = ConfigStore.CW_HIGHLIGHT_JS_PATH
        highlight_css_path = ConfigStore.CW_CSS_JS_PATH 

        # body
        html_template = f"""
        <html>
        <head>
            <style>
                body {{ 
                    {ConfigStore.RESPONSE_BOARD_STYLE_SHEET}
                    }}
            </style>
            <link rel="stylesheet" href="{highlight_css_path}">
            <script src="{highlight_js_path}"></script>
            <script>hljs.initHighlightingOnLoad();</script>
        </head>
        <body>
            {html_text}
        </body>
        </html>
        """


        ## HTMLを表示
        self.browser.setHtml(html_template, baseUrl=QUrl("file:///"))

    def toggle_response_view(self):
        '''
        レスポンス表示板の表示切り替えをします。
        (markdown対応)＜ー＞(streaming対応)
        '''
        # markdown対応が表示中か
        if self.browser.isVisible():
            self.browser.hide()
            self.preview_text.show()
        else:
            self.browser.show()
            self.preview_text.hide()

        # 状態をログ出力
        self.console.outputText(f"self.browser.isVisible():{self.browser.isVisible()}")
        self.console.outputText(f"self.preview_text.isVisible():{self.preview_text.isVisible()}")

    def previewText(self, text):
        '''
        速報的にレスポンスを出力します。
        '''

        self.preview_text.appendAddText(text)
        QApplication.processEvents()

    def resetPreviewText(self):
        '''
        速報板のメッセージを削除します。
        '''
        # self.preview_text = StreamQText()
        self.preview_text.clear()
        # self.preview_text.hide()

    def showPrompt(self, prompt):
        '''
        promptを表示します。
        '''
        self.previous_prompt_area.clear()
        self.previous_prompt_area.setText(prompt)
