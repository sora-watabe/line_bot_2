import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file=open("info.json","r")
info=json.load(file)

CANNEL_ACCESS_TOKEN=info['CANNEL_ACCESS_TOKEN']
line_bot_api=LineBotApi(CANNEL_ACCESS_TOKEN)

def main():
    USER_ID=info['USER_ID']
    messages=TextSendMessage(text='今日もお疲れ様！ \nいい夢見てなー')
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__ == "__main__":
    main()
    
