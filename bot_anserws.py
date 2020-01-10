from login_data import bot_token, api_hash, api_id, target_id
from telethon import TelegramClient, events
from session import PidFile

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
pid_file = PidFile('main.pid')
target_id = int(target_id)

@bot.on(events.NewMessage(chats=[target_id]))
async def new_message_handler(event):
    if event.raw_text == "/botstatus":
        if pid_file.check_if_exists():
            await bot.send_message(target_id, "Bot is currently online and is looking for new alerts")
        else:
            await bot.send_message(target_id, "Bot is currently offline and won't send any alerts.")

bot.run_until_disconnected()