from telethon import TelegramClient, events, sync
from telethon.sync import TelegramClient
from plugins import hello, result
from functions import add_mins, Error_handler

client = TelegramClient('anon', 123, '123')
client.start()

client.add_event_handler("hello.py", events.NewMessage)
client.add_event_handler("result.py", events.NewMessage)



client.run_until_disconnected()