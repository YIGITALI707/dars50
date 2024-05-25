from dotenv import load_dotenv
load_dotenv()
from aiogram import Dispatcher,executor,Bot
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboard import home_buttons
from course import save


import os
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start(message):
    await bot.send_message(message.from_user.id, 'Kerakli valyuta kursini tanlang', reply_markup=home_buttons)

@dp.message_handler(text="Dollar kursi 🇺🇸")
async def  dollar_info(message):
    course = save()
    await bot.send_message(message.from_user.id, 
                     f"<b>Bugungi dollar kursi: </b>\n {course[0]["Rate"]}\n <i>Sana:</i> {course[0]["Date"]}"
                    ,parse_mode="HTML")
    # await bot.send_message(message.from_user.id,message.text)

@dp.message_handler(text="Rubl kursi 🇷🇺")
async def  rubl_info(message):
    course = save()
    await bot.send_message(message.from_user.id, 
                     f"<b>Bugungi rubl kursi: </b>\n {course[2]["Rate"]}\n <i>Sana:</i> {course[2]["Date"]}"
                    ,parse_mode="HTML")

@dp.message_handler()
async def  info(message):
    print()
    print(message)
    print()
    await bot.send_message(message.from_user.id, "Botdan foydalanish uchun kerakli tugmalarni bosing !")
        
executor.start_polling(dp ,skip_updates=True)

