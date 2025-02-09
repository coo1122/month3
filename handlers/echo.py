from aiogram import types, Dispatcher



# @dp.message_handler()
async def echo_handler(message:types.Message):
    if message.text.isdigit():
        squared=int(message.text)**2
        await message.answer(str(squared))
    else:
        await message.answer(str(message.text))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)