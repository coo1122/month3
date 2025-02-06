from aiogram import types, Dispatcher, Bot, executor
from decouple import config
import logging

token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)

Admins=[918776187, ]

@dp.message_handler(commands="start")
async def start_handler(message:types.Message):
    print("Обработчик старта")
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой Telegram ID- {message.from_user.id}\n')

    await message.answer('Привет Мир')


@dp.message_handler(commands="mem")
async def start_handler2(message:types.Message):
    # photo=open("media/image1.png","rb")
    with open("media/image1.png","rb") as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)

@dp.message_handler()
async def echo(message:types.Message):
    await message.answer(message.text)
















if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)