
@client.on(events.NewMessage(outgoing=True, pattern=".google"))
async def find(event):
    query = event.raw_text.replace(".find ", "").replace(" ", "+")
    googlelink = f"http://www.google.com/search?q={query}"
    ducklink = f"https://duckduckgo.com/?q={query}"
    await event.edit(f"[Google results]({googlelink})\n[Duck Duck Go results]({ducklink})")cc