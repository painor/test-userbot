from telethon.sync import TelegramClient
from plugins import hello, result

client = TelegramClient('anon', 123, '123')
client.start()

client.add_event_handler(hello.haste)
client.add_event_handler(result.find)

client.run_until_disconnected()
