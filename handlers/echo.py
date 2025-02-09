from aiogram import types, Dispatcher

games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def echo_handler(message: types.Message):
    if message.text.isdigit():
        squared = int(message.text) ** 2
        await message.answer(str(squared))
    elif message.text.lower() == "game":
        await message.answer_dice(emoji='🎲')
    else:
        await message.answer(message.text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
