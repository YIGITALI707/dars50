from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
home_buttons=ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
dollar_btn=KeyboardButton("Dollar kursi")
rubl_btn=KeyboardButton("Rubl kursi")
evro_btn=KeyboardButton("Evro kursi")
home_buttons.add(dollar_btn)
home_buttons.add(evro_btn)
home_buttons.add(rubl_btn)
