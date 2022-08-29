import requests

def telegram_bot_sendtext(bot_message):

   bot_token = '1464229414:AAFr8arSPcY_4PTnazb6cpRtjnLxpLafm7s'
   bot_chatID = '642162627'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)