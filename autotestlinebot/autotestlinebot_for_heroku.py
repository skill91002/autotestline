from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage, TextSendMessage

import random
import time


linebot_client = LineBotApi("/diBCY/NIHQdUmXML33amlI/a6j8JQva55yTjB4RjTkBjckI2PxItJRh8vRk1n9Eo6fVJoTFCX+aBDBQvRnJtfrV1KUUbMVTXCvdts0AoRC30Mbe2rDe3GRGQksXVwxjqfK6NdWOHdnQPcjGa8+SFAdB04t89/1O/w1cDnyilFU=")
linebot_handler = WebhookHandler("3a7f225af653746219179110ad663f74")

app = Flask(__name__)


# 當人有呼叫 https://your-app-name.herokuapp.com/callback 時，會跑進來這，
# 這支函數是當 Message API 將資料送過來時，必須先做的處理（先照抄就好）
@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        linebot_handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'ok'


# 當有人傳純文字訊息給機器人時，會從 callback 導進來這，
# 這裡也是我們可以大肆搞鬼的地方
@linebot_handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):

    # 當 LINE 後台發送測試訊號過來時，會使用一組假 token，無視它就好
    if event.reply_token == '0' * 32:
        return

    # 暫停 1.5 秒，假裝在打字或讀訊息
    time.sleep(1.5)

    # 隨機回覆一串敷衍訊息
    linebot_client.reply_message(
        event.reply_token,
        TextSendMessage(
            random.choice([
                '好',
                'ok',
                '恩～',
                '我知道了',
            ])
        )
    )


if __name__ == '__main__':
    # 啟動 WEB 服務
    app.run(debug=True)

