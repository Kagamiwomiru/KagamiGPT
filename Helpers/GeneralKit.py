# そのほかの処理を定義
import subprocess
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QTextCursor
import tiktoken
from tiktoken.core import Encoding

class StreamQText(QTextEdit):
    def __init__(self, parent=None):
        super(StreamQText, self).__init__(parent)
        self.hide()
 
    def appendAddText(self, text):
        '''
        テキストを追加
        '''
        # 現在のテキストの末尾に新しいテキストを追加
        self.moveCursor(QTextCursor.End)
        self.insertPlainText(text)

    def resetText(self):
        '''
        空のテキストを入れる
        '''
        self.append("")


def get_version(repository):

    cmd = "cd %s && git tag" % repository
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    stdout_data = proc.stdout.read()


    if stdout_data:
        return stdout_data.decode().strip()
    else:
        print('cannot find tags.')
        return "N/A"
    


def estimateToken(model, text):
    '''
    トークン数を計算します。
    REF:https://dev.classmethod.jp/articles/openai-api-chatgpt-tiktoken/

    Parameters
    ---
    model   :   str
        モデル名
    text   :   str
        テキスト

    Return
    ---
    num_token   :   int
        トークン数
    '''

    encoding: Encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    num_token = len(tokens)
    return num_token
