# importing all required libraries 
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram as described above 
api_id = '2352156'
api_hash = '666de4c883b639ef5b13f87bd615bce8'
token = '1415543455:AAG2i-xttKYeZI1w2rWof3JeGgDIOv_mn3s'

# your phone number 
phone = '+917994805210'

message = 'hi albert'

receiver = []
# creating a telegram session and assigning 
# it to a variable client 
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session 
client.connect()

# in case of script ran first time it will 
# ask either to input token or otp sent to 
# number or sent or your telegram id
if not client.is_user_authorized():
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))


for d in client.iter_dialogs():
    print(d.name + ": " + str(d.entity.id))
    receiver.append(d.entity.id)

client.send_message(receiver, message, parse_mode='html')
# disconnecting the telegram session 
client.disconnect() 
