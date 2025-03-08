# main.py
from aiogram import executor
import logging
from handlers import commands, echo, quiz, FSM_registration, FSM_shop, send_products, delete_products, edit_products, admin_group
from config import dp, Admins, bot
import buttons
from db import main_db

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!', reply_markup=buttons.start)
        await main_db.create_tables()
        await main_db.create_tables_store()
        await main_db.create_tables_products_details()
        await main_db.create_tables_collection_products()


async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот выключен!')


# ====================================================================
commands.register_handlers(dp)
quiz.register_handlers(dp)
FSM_registration.register_handlers_fsm(dp)
FSM_shop.register_handlers_fsm(dp)

send_products.register_handlers(dp)
delete_products.register_handlers(dp)
edit_products.register_handlers(dp)
admin_group.register_handlers(dp)

# ==========================
echo.register_handlers(dp)
# ====================================================================


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)