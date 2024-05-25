from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

home = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

home.add( KeyboardButton("Shikoyat jo'natish 👎") )
home.add( KeyboardButton("Taklif jo'natish ✍️") )
