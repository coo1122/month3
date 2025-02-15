# buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


cancel_fsm = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('отмена'))



start = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
quiz_buttons = KeyboardButton('/quiz')
reg_buttons = KeyboardButton('/registration')
shop_buttons = KeyboardButton('/shop')
start.add(start_buttons, mem_buttons, quiz_buttons, reg_buttons, shop_buttons)


# Удаление кнопок из интерфейса
remove_keyboard = ReplyKeyboardRemove()

submit = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
yes = KeyboardButton('да')
no = KeyboardButton('нет')
submit.add(yes, no)