from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Далее', callback_data='quiz_2')
    keyboard.add(button)

    question = 'Какое время года?'
    answer = ['Лето', 'Зима', 'Осень', 'Весна']

    with open('media/test.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='🍂',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Завершить', callback_data='end_quiz')
    keyboard.add(button)

    question = 'Dota2 or CS.GO'
    answer = ['Dota2', 'CS.GO', 'Valve']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        reply_markup=keyboard
    )



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
