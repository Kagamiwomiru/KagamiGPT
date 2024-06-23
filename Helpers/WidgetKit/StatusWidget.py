from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout
from Helpers.DataKit import ConfigStore, ValueStore
from Helpers.DataKit.TextStore import StatusLabels
import yfinance as yf

class StatusWidget(QWidget):
    def __init__(self, console, parent=None):
        super(StatusWidget, self).__init__(parent)
        self.console = console
        ## 状態
        self.token_label = QLabel(StatusLabels.PW_TOKEN_TITLE_LABEL.value)
        self.token_prompt_label = QLabel(f"{StatusLabels.PW_TOKEN_PROMPT_LABEL.value} : {ValueStore.prompt_tokens}")
        self.token_completion_label = QLabel(f"{StatusLabels.PW_TOKEN_COMPLETION_LABEL.value} : {ValueStore.completion_tokens}")
        self.token_total_label = QLabel(f"{StatusLabels.PW_TOKEN_TOTAL_LABEL.value} : {ValueStore.total_tokens}")
        self.token_price_label = QLabel(f"{StatusLabels.PW_TOKEN_PRICE_LABEL.value} : ￥{ValueStore.price}")
           
        # レイアウトの定義
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.token_label, 0, 0)
        layout.addWidget(self.token_prompt_label, 1, 0)
        layout.addWidget(self.token_completion_label, 2, 0)
        layout.addWidget(self.token_total_label, 3, 0)
        layout.addWidget(self.token_price_label, 4, 0)


    def updateTokenStatus(self):
        '''
        ステータス情報を更新します。
        '''
        ValueStore.price = self.calcPrice()
        self.token_prompt_label.setText(f"{StatusLabels.PW_TOKEN_PROMPT_LABEL.value} : {ValueStore.prompt_tokens}")
        self.token_completion_label.setText(f"{StatusLabels.PW_TOKEN_COMPLETION_LABEL.value} : {ValueStore.completion_tokens}")
        self.token_total_label.setText(f"{StatusLabels.PW_TOKEN_TOTAL_LABEL.value} : {ValueStore.total_tokens}")
        self.token_price_label.setText(f"{StatusLabels.PW_TOKEN_PRICE_LABEL.value} : 約￥{round(ValueStore.price, ConfigStore.SIG_DIGS)}")
        

    def calcPrice(self):
        '''
        消費したトークンを円換算します。
        [出典]
        モデル：https://openai.com/pricing
        円/ドル：
        '''
        ticker = "USDJPY=X"
        try:
            data = yf.Ticker(ticker).history(period="1d")
            crate = data.Close.iloc[0]
            self.console.outputText("[Token Rate]")
            self.console.outputText(f"USD->YEN: {round(crate, ConfigStore.SIG_DIGS)}")
            self.console.outputText(f"input:{round(ConfigStore.MODEL_PRICE[ConfigStore.OPENAI_MODEL]['input'] * 1000, ConfigStore.SIG_DIGS)} /1K tokens")
            self.console.outputText(f"output:{round(ConfigStore.MODEL_PRICE[ConfigStore.OPENAI_MODEL]['output'] * 1000, ConfigStore.SIG_DIGS)} /1K tokens")



            # 計算
            price = (ConfigStore.MODEL_PRICE[ConfigStore.OPENAI_MODEL]["input"] * ValueStore.prompt_tokens \
                    + ConfigStore.MODEL_PRICE[ConfigStore.OPENAI_MODEL]["output"] * ValueStore.completion_tokens) \
                    * round(crate, ConfigStore.SIG_DIGS)
        except:
            print("為替情報の取得に失敗")
            price = 0.0
        
        return price

