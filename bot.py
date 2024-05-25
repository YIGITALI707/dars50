from dotenv import load_dotenv
load_dotenv()
from aiogram import Dispatcher,executor,Bot
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboard import home_buttons

import os
Token=os.getenv("Token")
bot=Bot(token=Token)
dp=Dispatcher(bot)
@dp.message_handler(CommandStart())
async def start(message):
    course=get
    await bot.send_message(message.from_user.id,"kerakli valyutani tanlang",reply_markup=home_buttons)
    f"Bugungi dollar kursi:\n {cou}"
@dp.message_handler(text="Dollar kursi")
async def dollar_info(message):
     await bot.send_message(message.from_user.id,"Dollar kursi 12500")



executor.start_polling(dp,skip_updates=True)


