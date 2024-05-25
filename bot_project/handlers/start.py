from main import dp, bot
from aiogram.dispatcher.filters.builtin import CommandStart


# from aiogram.filters.command import Command

@dp.message_handler(CommandStart())
async def start_bot2(message):
    print()
    print("Start")
    print()
    bot.send_message(message.from_user.id, " Hello")


async def on_startup(message):
    print()
    print("Bot ishga tushdi ")
    print()
