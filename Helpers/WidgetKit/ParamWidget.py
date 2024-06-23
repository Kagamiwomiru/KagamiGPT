from PyQt5.QtWidgets import QLabel, QWidget, QComboBox, QSlider, QSpinBox, QGridLayout, QCheckBox
from PyQt5.QtCore import Qt
from Helpers.DataKit import ConfigStore, ValueStore
from Helpers.DataKit.TextStore import ParamLabels

class ParamWidget(QWidget):
    '''
    モデルパラメーターを操作
    '''
    def __init__(self, console, parent=None):
        super(ParamWidget, self).__init__(parent)
        self.console = console
        # レイアウトの定義
        layout = QGridLayout()
        self.setLayout(layout)

        # 各項目の定義
        ## モデル
        self.model_combo_box = QComboBox()
        self.model_combo_box.addItems(ConfigStore.MODEL_LISTS)
        self.model_combo_box.setCurrentText(ConfigStore.OPENAI_MODEL)
        self.model_combo_box.currentIndexChanged.connect(self.setModelValue)
        self.model_label = QLabel(ParamLabels.PW_MODEL_INFO.value)
        self.model_combo_box.setToolTip(ParamLabels.UI_HOVER_TOOLTIP_MODEL_INFO.value)


        ## temperature
        self.temperature_slider = QSlider(Qt.Horizontal)
        ### intしか受け付けないので後段処理で1/10する。
        self.temperature_slider.setMinimum(0)
        self.temperature_slider.setMaximum(10)
        self.temperature_slider.setValue(ConfigStore.PW_TEMPERATURE_DEFAULT_VALUE)
        ValueStore.temperature = self.temperature_slider.value() / 10
        self.temperature_label = QLabel(f"Temperature:")
        self.temperature_slider.setToolTip(ParamLabels.UI_HOVER_TOOLTIP_TEMPERATURE.value)
        self.temperature_value_label = QLabel(str(ValueStore.temperature))
        ## 値が変更された時
        self.temperature_slider.valueChanged.connect(self.setTemperatureValue)

        ## Max token
        self.max_token_spinbox = QSpinBox()
        self.max_token_spinbox.setMinimum(ConfigStore.PW_MAX_TOKEN_MINIMUM_VALUE)
        self.max_token_spinbox.setMaximum(ConfigStore.PW_TEMPERATURE_MAXMUM_VALUE)
        self.max_token_spinbox.setValue(ConfigStore.PW_MAX_TOKEN_DEFAULT_VALUE)
        ValueStore.max_token = self.max_token_spinbox.value()
        self.max_token_label = QLabel(f"Max Token:")
        self.max_token_spinbox.setToolTip(ParamLabels.UI_HOVER_TOOLTIP_MAXTOKEN.value)
        ## 値が変更された時
        self.max_token_spinbox.valueChanged.connect(self.setMaxTokenValue)

        ## num memory
        self.num_memory_spinbox = QSpinBox()
        self.num_memory_spinbox.setMinimum(ConfigStore.PW_NUM_MEMORY_MINIMUM_VALUE)
        self.num_memory_spinbox.setMaximum(ConfigStore.PW_NUM_MEMORY_MAXMUM_VALUE)
        self.num_memory_spinbox.setValue(ConfigStore.PW_NUM_MEMORY_DEFAULT_VALUE)
        self.setNumMemoryValue()
        self.num_memory_label = QLabel(f"記憶するやり取りの数:")
        ## 値が変更された時
        self.num_memory_spinbox.valueChanged.connect(self.setNumMemoryValue)

        # streamingモード
        self.streaming_chkbox = QCheckBox()
        self.streaming_chkbox.setChecked(ConfigStore.IP_OPENAI_STREAM)
        ## 値が変更された時
        self.streaming_chkbox.stateChanged.connect(self.setChkValue)
        self.streaming_label = QLabel(f"Streaming Mode:")
        self.streaming_chkbox.setToolTip(ParamLabels.UI_HOVER_TOOLTIP_STREAMING.value)

        # widgetを設置
        layout.addWidget(self.model_label,0, 0)
        layout.addWidget(self.model_combo_box,0, 1)
        layout.addWidget(self.temperature_label, 1, 0)
        layout.addWidget(self.temperature_slider, 1, 1)
        layout.addWidget(self.temperature_value_label, 1, 2)
        layout.addWidget(self.max_token_label, 2, 0)
        layout.addWidget(self.max_token_spinbox, 2, 1)
        layout.addWidget(self.num_memory_label, 3, 0)
        layout.addWidget(self.num_memory_spinbox, 3, 1)
        layout.addWidget(self.streaming_label, 4, 0)
        layout.addWidget(self.streaming_chkbox, 4, 1)
        

    # 値更新
    def setModelValue(self):
        ConfigStore.OPENAI_MODEL = self.model_combo_box.currentText()
        self.console.outputText(f"Model:{str(ConfigStore.OPENAI_MODEL)}")

    def setTemperatureValue(self):
        ValueStore.temperature = self.temperature_slider.value() / 10
        self.temperature_value_label.setText(str(ValueStore.temperature))
        self.console.outputText(str(ValueStore.temperature))

    def setMaxTokenValue(self):
        ValueStore.max_token = self.max_token_spinbox.value() 
        self.console.outputText(f"Max token:{str(ValueStore.max_token)}")

    def setNumMemoryValue(self):
        ValueStore.num_memory = self.num_memory_spinbox.value() 
        self.console.outputText(f"Num memory:{str(ValueStore.num_memory)}")

    def setChkValue(self):
        ConfigStore.IP_OPENAI_STREAM = self.streaming_chkbox.checkState() == Qt.Checked
        self.console.outputText(f"ConfigStore.IP_OPENAI_STREAM :{str(ConfigStore.IP_OPENAI_STREAM)}")

