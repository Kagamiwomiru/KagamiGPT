# PDFとプロンプトを入力とするタブ

from Helpers.TabKit.BaseTab import BaseTab


class PDFChatTab(BaseTab):
    def __init__(self):
        super().__init__()

    # widgetの読み込み
    chat_widget = ChatWidget(console_widget)
    status_widget = StatusWidget(console_widget)
    param_widget = ParamWidget(console_widget)
    input_prompt_widget = InputPromptWidget(console_widget, chat_widget, status_widget)