# tab1
from Helpers.TabKit.BaseTab import BaseTab
from Helpers.WidgetKit.ImageAreaWidget import ImageAreaWidget
from Helpers.WidgetKit.ConsoleWidget import ConsoleWidget
from Helpers.WidgetKit.ParamWidget import ParamWidget
from Helpers.WidgetKit.InputPromptWidget import InputPromptWidget
from Helpers.WidgetKit.ChatWidget import ChatWidget
from Helpers.WidgetKit.StatusWidget import StatusWidget
from Helpers.DataKit.TextStore import TabLabels



class NormalChatTab(BaseTab):
    def __init__(self):
        super().__init__()
        
        # Widgetの読み込み
        console_widget = ConsoleWidget()
        chat_widget = ChatWidget(console_widget)
        status_widget = StatusWidget(console_widget)
        image_area_widget = ImageAreaWidget(console_widget)
        param_widget = ParamWidget(console_widget)
        input_prompt_widget = InputPromptWidget(console_widget, chat_widget, status_widget)

        # dockの定義
        img_area_dock = self.addWidget(image_area_widget, TabLabels.TAB1_DOCK1.value, size=(1, 10))
        param_dock = self.addWidget(param_widget, TabLabels.TAB1_DOCK2.value, size=(1, 10))
        chat_dock = self.addWidget(chat_widget, TabLabels.TAB1_DOCK3.value, size=(50, 10))
        prompt_dock = self.addWidget(input_prompt_widget, TabLabels.TAB1_DOCK4.value, size=(50, 1))
        log_dock = self.addWidget(console_widget, TabLabels.TAB1_DOCK5.value, size=(1, 1))
        status_dock = self.addWidget(status_widget, TabLabels.TAB1_DOCK6.value, size=(1,5))

        # dockのレイアウト
        self.area.addDock(chat_dock)
        self.area.addDock(param_dock, 'right', chat_dock)
        self.area.addDock(status_dock, 'bottom', param_dock)
        self.area.addDock(img_area_dock, 'bottom',status_dock) 
        self.area.addDock(prompt_dock, 'bottom',chat_dock)
        self.area.addDock(log_dock, 'bottom')



