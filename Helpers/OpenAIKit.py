# OpenAI関連
from Helpers.DataKit import ConfigStore, ValueStore
import base64
from openai import OpenAI


def initAI(ai_setting):
    '''
    AIの初期化処理
    会話設定もここでやる。
    （会話設定を変えるたびにこの処理が走るようにすること）

    Parameters
    ---
    ai_setting  :   str
        会話設定テキスト

    
    '''
    #メモ；https://platform.openai.com/docs/guides/vision

    # ValueStore.headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {ConfigStore.OPENAI_API_KEY}"
    # }
    # OpenAIクライアントの有効化
    ValueStore.client = OpenAI(api_key=ConfigStore.OPENAI_API_KEY)
    ValueStore.openai_api_version = ValueStore.client._version
    ValueStore.messages = [{
                                "role": "system",
                                "content": ai_setting
                            }]

def encodeImage():
    '''
    入力画像をbase64でエンコードします。
    '''
    with open(ValueStore.image_filepath, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
 
def RunOpenAI(stream=False):
    '''
    OpenAIに繋いで、内容を実行します。
    
    Parameters
    ---
    stream  :   bool
        OpenAIのStream機能を有効にするか？


    Returns
    ---
    stream == True
        chunk
    
    stream == False
        response
    '''



    
    # 画像のエンコード
    if ValueStore.image_filepath != "":
        base64_image = encodeImage()
        ValueStore.messages.append(
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": ValueStore.prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                   'url' : f"data:image/jpeg;base64,{base64_image}",
                                }
                            },
                        ]
                    }
                )
    else:
        # 画像が入力されていない時
        ValueStore.messages.append(
                    {
                        'role': 'user',
                        'content': [
                            {
                                "type": "text",
                                "text": ValueStore.prompt,
                            }
                        ]
                    },
                )
                        
    # langchainがopenai==1.0に非対応なので0.28の書き方にする
    return ValueStore.client.chat.completions.create(model=ConfigStore.OPENAI_MODEL,
    messages=ValueStore.messages,
    # ストリームを有効化する場合は`True`
    stream=stream,
    temperature=ValueStore.temperature,
    max_tokens=ValueStore.max_token)

   
    # return requests.post("https://api.openai.com/v1/chat/completions",
                            # headers=ValueStore.headers, json=payload)




def main():
    import argparse
    parser = argparse.ArgumentParser(description='OpenAIテストプログラム') 
    parser.add_argument('-p','--prompt', help='プロンプト',required=True)    
    parser.add_argument('-i','--input_file', help='画像')
    args = parser.parse_args() 

    initAI()
    ValueStore.prompt = args.prompt
    ValueStore.image_filepath = args.input_file
    ValueStore.max_token = 800
    ValueStore.temperature = 0.5
    response = RunOpenAI()
    print(f"AI: {response.json()}")
if __name__ == "__main__":
    main()
   