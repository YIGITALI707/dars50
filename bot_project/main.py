import os
from dotenv import load_dotenv
from aiogram import executor,Dispatcher,Bot
from aiogram.dispatcher.filters.builtin import CommandStart
# from  handlers import on_startup
from database.db import Database
from buttons.home import home

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database()

@dp.message_handler(CommandStart())
async def start_bot(message):

    tg_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    if not db.users_exists(tg_id):
        db.add_user(tg_id, username, first_name, last_name)
        await bot.send_message(message.from_user.id,"Salom xush kelibsiz! \n Shikoyat yoki taklif jo'natish uchun kerakli tugmani tanlang", reply_markup=home)
    else:
        await bot.send_message(message.from_user.id,"Qaytib keldizmi? \n Shikoyat yoki taklif jo'natish uchun kerakli tugmani tanlang", reply_markup=home)

if __name__ == '__main__':
    executor.start_polling(dp )
