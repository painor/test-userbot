
@client.on(events.NewMessage(outgoing=True, pattern=".hihello$"))
async def haste(event):
    await event.edit("Hello, It's test message, again me.")
