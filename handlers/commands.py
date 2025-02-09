from aiogram import types, Dispatcher
from config import bot



# @dp.message_handler(commands="start")
async def start_handler(message:types.Message):
    print("Обработчик старта")
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой Telegram ID- {message.from_user.id}\n')

    await message.answer('Привет Мир')


# @dp.message_handler(commands="mem")
async def mem_handler(message:types.Message):
    # photo=open("media/image1.png","rb")
    with open("media/image1.png","rb") as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(mem_handler, commands=["mem"])