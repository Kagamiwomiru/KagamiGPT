import os
import configparser
import sys
from Helpers.GeneralKit import get_version
# ConfigStore.py
APP_ROOT_PATH = os.getcwd()
# アプリケーション設定情報
# dpath = os.path.dirname(sys.argv[0]) # 追加
if getattr(sys, 'frozen', False):
    # 実行ファイルからの実行時
    APP_ROOT_PATH = sys._MEIPASS
else:
    # スクリプトからの実行時
    APP_ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../")

CONFIG_PATH = os.path.join(APP_ROOT_PATH, "config.ini")
CONFIG_PARSER = configparser.ConfigParser()
CONFIG_PARSER.read(CONFIG_PATH)
## OpenAI設定
OPENAI_API_KEY = CONFIG_PARSER['DEFAULT']['OPENAI_API_KEY']
OPENAI_MODEL = CONFIG_PARSER['DEFAULT']['DEFAULT_MODEL']
MODEL_LISTS = [
    "gpt-4o", # 最新版GPT4より安い
    "gpt-4-turbo", # GPT4-turbo画像もOK
    "gpt-3.5-turbo", # GPT3.5
]
# 1トークンあたり
# https://openai.com/pricing
MODEL_PRICE = {
    "gpt-4o":{
        "input": 0.000005,
        "output": 0.000015
    },
    "gpt-4-turbo":{
        "input": 0.00001,
        "output": 0.00003
    },
    "gpt-3.5-turbo":{
        "input": 0.0000005,
        "output": 0.0000015
    }
}
################################################

## MainWindow.py ##
APP_NAME = "KagamiGPT"
DEV_VERSION = get_version(APP_ROOT_PATH)
APP_VERSION = "2.5.2"
APP_AUTHOR = "Kagamiwomiru"
MAIN_WIN_WIDTH = 500
MAIN_WIN_HEIGHT = 400
TAB_ZERO_WIDTH = 500
TAB_ZERO_HEIGHT = 400
TAB_ONE_WIDTH = 1200
TAB_ONE_HEIGHT = 800



## MenuBar.py
APP_ICON = f"{APP_ROOT_PATH}/assets/img/appicon@2x.png"

## WidgetKit.py

PW_TEMPERATURE_DEFAULT_VALUE = 5
PW_MAX_TOKEN_DEFAULT_VALUE = 800
PW_MAX_TOKEN_MINIMUM_VALUE = 0
PW_NUM_MEMORY_MINIMUM_VALUE = 0
PW_NUM_MEMORY_MAXMUM_VALUE = 10
PW_NUM_MEMORY_DEFAULT_VALUE = 2
PW_TEMPERATURE_MAXMUM_VALUE = 9999

CW_HIGHLIGHT_JS_PATH = f"{APP_ROOT_PATH}/assets/js/highlight/highlight.js"  # Highlight.jsのパス
CW_CSS_JS_PATH = f"{APP_ROOT_PATH}/assets/js/highlight/styles/default.css"  # Highlight.jsのスタイルシートのパス

IP_OPENAI_STREAM = True # OpenAIのStreamを有効？

CHARACTER_DIR = f"{APP_ROOT_PATH}/Characters"
CHARCTER_EXTENSION = ".character" # キャラファイルの拡張子
FW_IMAGE_DIR = f"{APP_ROOT_PATH}/assets/img/face/"
FW_NODATA_IMG = f"{APP_ROOT_PATH}/assets/img/face/NO_DATA.png"

RESPONSE_BOARD_STYLE_SHEET = "background-color: white; font-family: Hiragino Sans W4,Arial, sans-serif; color: black; font-size: 12px;"
PREVIOUS_PROMPT_STYLE_SHEET = "font-size: 10px;"


# CharacterKit.py
CE_WINDOW_SIZE = {
    "width" :   800,
    "height"    :   500
}

# 記憶数
NUM_MEMORY = 2

# アプリケーション設定
CS_GROUP = "DEFAULT"
CS_ITEM_OPENAPI_KEY = "OPENAI_API_KEY"
CS_ITEM_GOOGLE_SEARCH_API_KEY = "GOOGLE_CUSTOM_SEARCH_API_KEY"
CS_ITEM_GOOGLE_SEARCH_ENGINE_ID = "GOOGLE_CUSTOM_SEARCH_ENGINE_ID"
CS_ITEM_DEFAULT_MODEL = "DEFAULT_MODEL"
CS_TEXT_MINIMUM_SIZE = 400

# 有効数字（桁）
SIG_DIGS = 3