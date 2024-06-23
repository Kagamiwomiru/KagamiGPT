from enum import Enum
class MainWindowLabels(Enum):
    MAIN_WIN_TAB0 = "Compact"
    MAIN_WIN_TAB1 = "Normal"
    MAIN_WIN_TAB2 = "PDF"


class TabLabels(Enum):
    TAB1_DOCK1 = "入力画像"
    TAB1_DOCK2 = "パラメータ"
    TAB1_DOCK3 = "チャット"
    TAB1_DOCK4 = "プロンプト"
    TAB1_DOCK5 = "ログ"
    TAB1_DOCK6 = "ステータス"
    TAB1_DOCK7 = "人格設定"


class MenuBarLabels(Enum):
    MB_EDIT_CUSTOM_LABEL = "キャラクター設定"
    MB_TOOL_TIKTOKEN_LABEL = "トークン計算機"
    MB_CONFIG_WINDOW_LABEL = "アプリケーション設定"


class CharacterWindowLabels(Enum):
    CE_WINDOW_TITLE = MenuBarLabels.MB_EDIT_CUSTOM_LABEL.value
    CE_FILELIST_LABEL = "キャラクターファイル一覧"
    CE_TEXTEDITOR_LABEL = "設定ファイル"
    CE_EDITER_CONTEXT_RENAME_LABEL = "キャラクター名称の変更"
    CE_EDITER_CONTEXT_DELETE_LABEL = "キャラクターを削除"
    CE_EDITER_RENAME_DIALOG_LABEL = "新しい名称を入力してください。"
    CE_EDITER_REMOVE_CHECK_TITLE = "キャラクターデータの削除"
    CE_EDITER_REMOVE_CHECK_MSG = "キャラクターデータを削除してよろしいですか？"
    CE_EDITER_INFO = '''
    [ai_setting]
    ここに入力した文章もプロンプトと同様にトークンを消費します。
    英語を使った方が消費トークンを節約できます。

    [icon_filepath]
    アイコンのファイルパスを指定します。
    パスはアプリの現在位置からの相対パスを指定します。
    もしファイルが見つからなければ、ダミーアイコンが表示されます。
                    '''
    CE_NEWFILE_BUTTON = "新規キャラクター"
    CE_EDITER_BUTTON = "保存"


class TokenCalculaterLabels(Enum):
    TC_WINDOW_TITLE = MenuBarLabels.MB_TOOL_TIKTOKEN_LABEL.value
    TC_EDITER_INFO = "ここに文字列を入力されたトークン数を計算します。"
    TC_EDITER_BUTTON = "計算"
    TC_EDITER_LABEL = "トークン数："


class AppSettingLabels(Enum):
    CS_WINDOW_TITLE = MenuBarLabels.MB_CONFIG_WINDOW_LABEL.value
    CS_LABEL_CONFIGPATH = "Config.initのパス"
    CS_LABEL_OPENAPI_KEY = "OpenAI API Key:"
    CS_LABEL_GOOGLE_SEARCH_API_KEY = "Google Custom Search API Key:"
    CS_LABEL_GOOGLE_SEARCH_ENGINE_ID = "Google Custom Search Engine ID:"
    CS_LABEL_DEFAULT_MODEL = "Default Model:"
    CS_LABEL_SAVE_BUTTON = "保存"   


class WidgetKitLabels(Enum):
    '''
    各ウィジェットの基底クラス
    '''
    pass


class ImageAreaLabels(WidgetKitLabels):
    IA_LABEL = "ここに画像をドラッグ&ドロップ"
    IA_REMOVE_BUTTON = "画像を削除"

class InputPromptLabels(WidgetKitLabels):
    IP_RUN_BUTTON_LABEL = "送信"
    UI_HOVER_TOOLTIP_CHARACTER_INFO = '''
    セットする人格を選択します。
    これまでのやり取りはリセットされます。
    '''

class StatusLabels(WidgetKitLabels):
    PW_TOKEN_TITLE_LABEL = "[消費トークン]"
    PW_TOKEN_PROMPT_LABEL = "プロンプト"
    PW_TOKEN_COMPLETION_LABEL = "AI"
    PW_TOKEN_TOTAL_LABEL = "合計"
    PW_TOKEN_PRICE_LABEL = "支払い金額"


class ParamLabels(WidgetKitLabels):
    PW_TALK_CONF_INFO = "人格設定"
    PW_MODEL_INFO = "モデル"

    UI_HOVER_TOOLTIP_MODEL_INFO = '''
    モデルを選択します。gpt4の方が高額ですが高性能です。
    "vision"とついているモデルは、画像入力ができます。
    '''

    UI_HOVER_TOOLTIP_TEMPERATURE = '''
    この値を大きくするとモデルの創造性が上がります。
    (よりランダムな答えを出すようになります。)
    '''

    UI_HOVER_TOOLTIP_MAXTOKEN = '''
    AIが消費する最大トークン数を指定します。
    （ユーザーが入力するトークン数ではありません）
    '''

    UI_HOVER_TOOLTIP_STREAMING = '''
    OpenAI APIのStreamingモードを有効にします。
    ログにストリーミングで出力が表示されるようになりますが、
    画像入力時のトークン数が正しくなくなります。
    '''

