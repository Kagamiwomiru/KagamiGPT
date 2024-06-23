from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout, QTextEdit, QPushButton, QComboBox
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from Helpers.DataKit import ConfigStore, ValueStore
from Helpers.DataKit.TextStore import InputPromptLabels
from Helpers.GeneralKit import estimateToken
from Helpers.CharacterKit import LoadCharacter, MakeCharacterList
from Helpers.OpenAIKit import RunOpenAI, initAI
import os


class InputPromptWidget(QWidget):
    def __init__(self, console, chat,status, parent=None):
        super(InputPromptWidget, self).__init__(parent)
        self.console = console
        self.chat = chat
        self.status = status

        self.layout = QGridLayout(self)
        # プロンプト部
        self.input_prompt = QTextEdit()
        self.input_prompt.installEventFilter(self)
        self.run_button = QPushButton(InputPromptLabels.IP_RUN_BUTTON_LABEL.value)
        self.run_button.clicked.connect(self.RunAI)
        self.run_button.setEnabled(False)
        
        # 人格設定部
        self.face_area = QLabel("NO_DATA")
        self.talk_config_combo_box = QComboBox()
        self.talk_config_combo_box.addItems(MakeCharacterList(ConfigStore.CHARACTER_DIR, extension=ConfigStore.CHARCTER_EXTENSION))
        self.setCharacterValue()
        self.talk_config_combo_box.currentIndexChanged.connect(self.setCharacterValue)
        self.talk_config_combo_box.setToolTip(InputPromptLabels.UI_HOVER_TOOLTIP_CHARACTER_INFO.value)

        
        # レイアウト
        self.layout.addWidget(self.face_area,0,0,alignment=Qt.AlignCenter)
        self.layout.addWidget(self.input_prompt,0,1)
        self.layout.addWidget(self.talk_config_combo_box,1,0)
        self.layout.addWidget(self.run_button,1,1)

    def eventFilter(self,obj, event):
        '''
        キーが押された時の処理を管理します。
        '''
        if obj is self.input_prompt and event.type() == event.KeyPress:
            if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Return:
                # Ctrl+enterが押された時の処理
                self.RunAI()
                return True  # イベントが処理されたことを示します
            elif self.input_prompt.toPlainText() == "" and Qt.ControlModifier and event.key() == Qt.Key_Up:
                # 何も入力内容が存在せず、上キーを押した時
                self.input_prompt.setText(self.chat.previous_prompt_area.text())
        elif self.input_prompt.toPlainText() == "":
                # 何も入力内容が存在しない時
                self.run_button.setEnabled(False)
        else:
            self.run_button.setEnabled(True)



        return False  # 他のイベントについてはデフォルトの処理を行います

    def setCharacterValue(self):
        '''
        人格設定をします。
        '''
        ValueStore.character = self.talk_config_combo_box.currentText()
        ai_setting, icon_filepath = LoadCharacter(ConfigStore.CHARACTER_DIR, ValueStore.character, extension=ConfigStore.CHARCTER_EXTENSION)
        self.load_image(os.path.join(ConfigStore.APP_ROOT_PATH, icon_filepath))
        initAI(ai_setting)
        self.console.outputText(f"Character:{str(ValueStore.character)}")

    def load_image(self, path):
        '''
        画像の読み込み
        '''
        if(os.path.isfile(path)):
            pixmap = pg.QtGui.QPixmap(path)
        else:
            pixmap = pg.QtGui.QPixmap(ConfigStore.FW_NODATA_IMG)
        # scaled_pixmap = pixmap.scaled(self.face_area.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        scaled_pixmap = pixmap.scaled(100,100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.face_area.setPixmap(scaled_pixmap)

    def showComboBox(self):
        '''
        コンボボックスが表示された時の処理
        '''
        self.talk_config_combo_box.clear()
        self.talk_config_combo_box.addItems(MakeCharacterList(ConfigStore.CHARACTER_DIR, extension=ConfigStore.CHARCTER_EXTENSION))



    def RunAI(self):

        ValueStore.prompt = self.input_prompt.toPlainText()
        self.input_prompt.clear()  # テキストをクリア
        self.console.outputText(f"input:{ValueStore.prompt}")


        # 最大記憶容量オーバー時には古い記憶を削除する。
        # （会話設定はidx==0に設定されているので、最も古いプロンプトidx==1と最も古いAIの解答idx==2を削除する。)
        # 無限ループ：終了条件：ValueStore.messagesが規定の数になるまで
        while True:
            if(len(ValueStore.messages) - 1 > ValueStore.num_memory * 2):
                del ValueStore.messages[1]
                del ValueStore.messages[1]
                self.console.outputText("Oblivion!!")
            else:
                break

        # PreviousPromptエリアにプロンプトを表示
        self.chat.showPrompt(ValueStore.prompt)


        # AIの実行
        response = RunOpenAI(stream=ConfigStore.IP_OPENAI_STREAM)

        if ConfigStore.IP_OPENAI_STREAM:
            # Stream有効
            next = []
            # レスポンス表示板の表示切り替え（streaming対応板）
            self.chat.toggle_response_view()
            # self.console.streamText("\noutput:")
            for chunk in response:
                try:
                    stream_text = chunk.choices[0].delta.content
                    if stream_text == None:
                        stream_text = ""
                    next.append(stream_text)
                    # print(next[-1], end='')
                    # self.console.streamText(next[-1])
                    self.chat.previewText(next[-1])
                except:
                    break
            
            ValueStore.answer = ''.join(next) # AIの解答
            # トークン数を計算
            # TODO:（人格設定）分のトークン数が未反映
            ValueStore.prompt_tokens = estimateToken(ConfigStore.OPENAI_MODEL, ValueStore.prompt) # プロンプトで消費したトークン
            ValueStore.completion_tokens = estimateToken(ConfigStore.OPENAI_MODEL, ValueStore.answer)  # AIが消費したトークン
            ValueStore.total_tokens = ValueStore.prompt_tokens + ValueStore.completion_tokens # 消費合計
           


        else:
            # Stream無効
            try:
                ValueStore.prompt_tokens = response.usage.prompt_tokens# プロンプトで消費したトークン
                ValueStore.completion_tokens = response.usage.completion_tokens  # AIが消費したトークン
                ValueStore.total_tokens = ValueStore.prompt_tokens + ValueStore.completion_tokens # 消費合計
                ValueStore.answer = response.choices[0].message.content # AIの解答
            except:
                ValueStore.answer = response.error.message # 要確認

        # AIの返答を記憶
        ValueStore.messages.append(
                    {
                        'role': 'assistant',
                        'content': [
                            {
                                "type": "text",
                                "text": ValueStore.answer,
                            }
                        ]
                    },
                
                )

        # ChatWidgetに結果を送信
        self.chat.compileText(ValueStore.answer)
        self.chat.resetPreviewText()
        # レスポンス表示板の表示切り替え（markdown対応板）
        self.chat.toggle_response_view()


        # StatusWidgetに情報を送信
        self.status.updateTokenStatus()

