import errno
import os
import configparser
import shutil
import sys
from glob import glob
import re
from Helpers.DataKit import ConfigStore, ValueStore
from Helpers.DataKit.TextStore import CharacterWindowLabels
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QTextEdit, QWidget, QSplitter, QListWidget, QLabel, QMenu, QAction, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def MakeCharacterList(character_dir, extension=".txt"):
    '''
    キャラファイルのリストを作成します。
    
    Paramerer
    ---
    character_dir   :   str
        キャラクターファイルが格納されたディレクトリ

    extension=".txt"   :   str
        キャラクタファイルの拡張子

    Return
    ---
    character_list  :   list
        キャラファイル一覧のリスト
    '''
    return [os.path.splitext(os.path.basename(file))[0] for file in sorted(glob(os.path.join(character_dir, '*' + extension)), key=natural_keys)]
    

def LoadCharacter(character_dir, character_name, extension=".txt"):
    '''
    キャラクターデータを読み込みます。

    Parameters
    ---
    character_dir   :   str
        キャラクターデータファイルが格納されたディレクトリ

    character_name  :   str
        キャラ名

    extension=".txt" :   str
        キャラクターデータファイルの拡張子


    Returns
    ---
    ai_setting  :   str
        会話設定

    icon_filepath   :   str
        キャラアイコンのファイルパス
    '''
    # ファイル読み込み
    character_data_filepath = os.path.join(character_dir, character_name + extension)
    if not os.path.exists(character_data_filepath):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), character_data_filepath)

    character_data_file = configparser.ConfigParser()
    character_data_file.read(character_data_filepath, encoding="utf-8")
    
    # データ読み込み
    character_data = character_data_file["CHARACTER DATA"]
    ai_setting = character_data.get("ai_setting")
    icon_filepath = character_data.get("icon_filepath")

    return ai_setting, icon_filepath


class CharacterEditerWindow(QWidget):
    '''
    人格設定ファイル編集画面
    以下の場合、このウインドウを閉じるとアプリが再起動します。
     - キャラクタファイルを生成する
     - キャラクタファイルの名称を変更する
     - キャラクターファイルを削除する。
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle(CharacterWindowLabels.CE_WINDOW_TITLE.value)
        self.setGeometry(300, 300, 
                         ConfigStore.CE_WINDOW_SIZE["width"], ConfigStore.CE_WINDOW_SIZE["height"])
        layout = QVBoxLayout()
        self.setLayout(layout)

        # アプリ再起動フラグ
        self.restartFlag = False

        # ファイルリスト
        self.fileListLabel = QLabel(CharacterWindowLabels.CE_FILELIST_LABEL.value)
        self.fileList = QListWidget()
        ## 右クリックメニュー
        self.fileList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fileList.customContextMenuRequested.connect(self.showContextMenu)
        ## 左クリック
        self.fileList.clicked.connect(self.onFileClicked)

        # テキストエディタ
        self.textEditorLabel = QLabel(CharacterWindowLabels.CE_TEXTEDITOR_LABEL.value)
        self.textEditor = QTextEdit()
        self.textEditor.setToolTip(CharacterWindowLabels.CE_EDITER_INFO.value)

        # 新規作成ボタン
        self.newButton = QPushButton(CharacterWindowLabels.CE_NEWFILE_BUTTON.value)
        self.newButton.clicked.connect(self.new_character)

        # 保存ボタン
        self.saveButton = QPushButton(CharacterWindowLabels.CE_EDITER_BUTTON.value)
        self.saveButton.clicked.connect(self.save_character)

        # スプリッターの作成
        self.splitter = QSplitter(self)

        # 左ペイン
        self.leftPane = QWidget()
        self.leftPaneLayout = QVBoxLayout(self.leftPane)
        self.leftPaneLayout.addWidget(self.fileListLabel)
        self.leftPaneLayout.addWidget(self.newButton)
        self.leftPaneLayout.addWidget(self.fileList)

        # 右ペイン
        self.rightPane = QWidget()
        self.rightPaneLayout = QVBoxLayout(self.rightPane)
        self.rightPaneLayout.addWidget(self.textEditorLabel)
        self.rightPaneLayout.addWidget(self.textEditor)
        self.rightPaneLayout.addWidget(self.saveButton)
        

        # スプリッターにウィジェットを追加
        self.splitter.addWidget(self.leftPane)
        self.splitter.addWidget(self.rightPane)

        # ウインドウ全体のレイアウトを作成
        layout.addWidget(self.splitter)
 

        # ペインサイズ
        # スプリッター全体のサイズを取得
        totalSize = ConfigStore.CE_WINDOW_SIZE["width"]
        # サイズ比を1:3に設定
        leftSize = totalSize // 4
        rightSize = totalSize - leftSize
        self.splitter.setSizes([leftSize, rightSize])

        
        # フォルダ内のファイルをリストに追加
        self.populateFileList(ConfigStore.CHARACTER_DIR)


    def closeEvent(self, event):
        # サブウインドウが閉じられるときの処理をここに書く
        if self.restartFlag == True:
            self.restartApplication()


    def restartApplication(self):
        # アプリケーションを再起動する
        QCoreApplication.quit()
        status = QCoreApplication.exec_()
        os.execv(sys.executable, ['python'] + sys.argv)


    def populateFileList(self, folderPath):
        try:
            # 指定されたフォルダ内のファイル一覧を取得
            files = os.listdir(folderPath)
            for filename in files:
                self.fileList.addItem(filename.split('.')[0])
        except FileNotFoundError:
            print(f"The folder '{folderPath}' does not exist.")

    def clearFileList(self):
        self.fileList.clear()


    def onFileClicked(self, index):
        # 選択されたファイルのパスを取得
        filename = self.fileList.item(index.row()).text()
        ValueStore.character_edit_filePath = os.path.join(ConfigStore.CHARACTER_DIR, filename + ConfigStore.CHARCTER_EXTENSION)

        try:
            # ファイルを開いて内容をテキストエディタに表示
            with open(ValueStore.character_edit_filePath, 'r', encoding='utf-8') as file:
                self.textEditor.setText(file.read())
        except Exception as e:
            print(f"Failed to open {filename}: {e}")


    def save_character(self):
        '''
        入力した内容で人格を設定します。
        '''

        # ファイルに書き出す。
        with open(ValueStore.character_edit_filePath, 'w') as F:
            F.write(self.textEditor.toPlainText())

        # print(f"EDIT_CHARACTER:{ValueStore.character_edit_filePath}")
        # アプリ再起動フラグON
        self.restartFlag = True

 

    def new_character(self):
        '''
        新規キャラクターを作成
        '''
        shutil.copy(os.path.join(ConfigStore.APP_ROOT_PATH, "Helpers", "DataKit", "skeleton.character"), os.path.join(ConfigStore.CHARACTER_DIR, "new_character.character"))
        # ファイルリスト更新
        self.clearFileList()
        self.populateFileList(ConfigStore.CHARACTER_DIR)

                
        # アプリ再起動フラグON
        self.restartFlag = True


    def showContextMenu(self, position):
        '''
        右クリックメニュー
        '''
        # リストアイテムの位置を取得
        index = self.fileList.indexAt(position)
        if not index.isValid():
            return

        # コンテキストメニューを作成
        menu = QMenu()

        # アクションを追加
        actionRename = QAction(CharacterWindowLabels.CE_EDITER_CONTEXT_RENAME_LABEL.value, self)
        actionDelete = QAction(CharacterWindowLabels.CE_EDITER_CONTEXT_DELETE_LABEL.value, self)
        menu.addAction(actionRename)
        menu.addAction(actionDelete)

        # アクションにシグナルを接続
        actionRename.triggered.connect(lambda: self.contextItemRenameFile(index))
        actionDelete.triggered.connect(lambda: self.contextItemDeleteFileDialog(index))

        # メニューを表示
        menu.exec_(self.fileList.mapToGlobal(position))


    def contextItemRenameFile(self, index):
        '''
        ファイル名を変更する
        '''

        # 現在のアイテムを取得
        item = self.fileList.itemFromIndex(index)

        # 新しい名前をユーザーに尋ねる
        old_name = item.text()
        new_name, ok = QInputDialog.getText(self, CharacterWindowLabels.CE_EDITER_CONTEXT_RENAME_LABEL.value, CharacterWindowLabels.CE_EDITER_RENAME_DIALOG_LABEL.value, text=old_name)

        # ユーザーがOKを押したらアイテムの名前を更新
        if ok and new_name:
            item.setText(new_name)
            os.rename(os.path.join(ConfigStore.CHARACTER_DIR, old_name + ConfigStore.CHARCTER_EXTENSION), 
                      os.path.join(ConfigStore.CHARACTER_DIR, item.text() + ConfigStore.CHARCTER_EXTENSION))
            
        # アプリ再起動フラグON
        self.restartFlag = True


    def contextItemDeleteFileDialog(self, index):
        '''
        ファイルを削除する
        '''
        # 現在のアイテムを取得
        item = self.fileList.itemFromIndex(index)

        # 削除して良いか確認
        removeCheckDialog = QMessageBox()
        removeCheckDialog.setIcon(QMessageBox.Question)
        removeCheckDialog.setWindowTitle(CharacterWindowLabels.CE_EDITER_REMOVE_CHECK_TITLE.value)
        removeCheckDialog.setText(CharacterWindowLabels.CE_EDITER_REMOVE_CHECK_MSG.value)
        removeCheckDialog.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
        response = removeCheckDialog.exec_()
                
 
        
        # OKが押されたらファイルを削除する。
        if response == QMessageBox.Ok:
            self.ItemDeleteFile(item)
            # ファイルリスト更新
            self.clearFileList()
            self.populateFileList(ConfigStore.CHARACTER_DIR)

    def ItemDeleteFile(self, item):
        '''
        ファイルを削除する
        '''
        print(os.path.join(ConfigStore.CHARACTER_DIR, item.text() + ConfigStore.CHARCTER_EXTENSION))
        os.remove(os.path.join(ConfigStore.CHARACTER_DIR, item.text() + ConfigStore.CHARCTER_EXTENSION))

        # アプリ再起動フラグON
        self.restartFlag = True
