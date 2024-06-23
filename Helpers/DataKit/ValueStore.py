# 各変数の値を管理します

# WidgetKit.ImageAreaWidget
image_filepath = "" 

# WidgetKit.StatusWidget
price = 0
# WidgetKit.ParamWidget
temperature = None
max_token = None
character = ""
character_config = ""
# WidgetKit.InputPromptWidget
prompt = ""
prompt_tokens = ""
completion_tokens = ""
system_tokens = ""
total_tokens = ""
answer = None
# WidgetKit.ChatWidget
markdown_text = \
'''
*ここにAIの答えが表示されます。*
'''
# 表示test用
# markdown_text = \
# '''
# # 見出し1

# ## 見出し2

# ### 見出し3

# #### 見出し4

# markdownサンプル文章です。ここは地の文です。

# markdownでは、箇条書きは*や-などの記号を文頭に置くことで記述します。箇条書きの階層は行頭スペース4つを足します。

# - これはひとつめの箇条書き
# - ふたつめの箇条書き
#     - 一つ階層が深い箇条書き
# - みっつめの箇条書き

# ### コード

# 3つのバッククォート記号でくくることで、コード例を示します

# ```python
# import sys
# print(sys.path)
# for i in range(i):
#     print(i)

# ```

# markdown形式については、Wikipediaなども参照ください
# - http://ja.wikipedia.org/wiki/Markdown
# '''


# OpenAIKit
headers = {}

response = ""

assistant_talk_history = []
openai_api_version = None

# CharacterKIt.py
custom_character = ""
character_edit_filePath = ""

# 記憶数
num_memory = 0