from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import main_db


class EditProducts(StatesGroup):
    for_field = State()
    for_new_photo = State()
    for_new_field = State()




async def start_send_products(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button_all = InlineKeyboardButton('Вывести все товары',
                                      callback_data='edit_all')
    button_one = InlineKeyboardButton('Вывести по одному',
                                      callback_data='edit_one')

    keyboard.add(button_all, button_one)

    await message.answer("Выберите каким образом хотите просмотреть товары:",
                         reply_markup=keyboard)



async def send_all_products(call: types.CallbackQuery):
    products = main_db.fetch_all_products()

    if products:
        for product in products:
            caption = (f'Название товара - {product["name_product"]}\n'
            f'Размер товара - {product["size"]}\n'
            f'Категория - {product["category"]}\n'
            f'Артикул - {product["productid"]}\n'
            f'Инфо - {product["infoproduct"]}\n'
            f'Цена - {product["price"]}')

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            edit_button = types.InlineKeyboardButton(
                'Редактировать', callback_data=f"edit_{product['productid']}")
            keyboard.add(edit_button)

            await call.message.answer_photo(photo=product["photo"],
                                            caption=caption,
                                            reply_markup=keyboard)
    else:
        await call.message.answer('Товаров нет!')


async def edit_product(call: types.CallbackQuery, state: FSMContext):
    productid = call.data.split('_')[1]

    await state.update_data(articul=productid)

    keyboard = types.InlineKeyboardMarkup(row_width=2)

    name_button = InlineKeyboardButton(text="Название", callback_data="field_name_product")
    category_button = InlineKeyboardButton(text="Категория", callback_data="field_category")
    price_button = InlineKeyboardButton(text="Цена", callback_data="field_price")
    size_button = InlineKeyboardButton(text="Размер", callback_data="field_size")
    photo_button = InlineKeyboardButton(text="Фото", callback_data="field_photo")
    info_button = InlineKeyboardButton(text="Инфо о товаре", callback_data="field_infoproduct")
    keyboard.add(name_button, category_button, price_button, size_button, photo_button, info_button)

    await call.message.answer('Выберите поле для редактирования:', reply_markup=keyboard)

    await EditProducts.for_field.set()


async def select_field_product(call: types.CallbackQuery, state: FSMContext):

    field_map = {
        'field_name_product': 'name_product',
        'field_category': 'category',
        'field_price': 'price',
        'field_size': 'size',
        'field_photo': 'photo',
        'field_infoproduct': 'infoproduct'
    }

    field = field_map.get(call.data)

    print(field)

    if not field:
        await call.message.answer('Недопустимое поле')
        return

    await state.update_data(field=field)

    if field == 'photo':
        await EditProducts.for_new_photo.set()
        await call.message.answer('Отправьте новое фото')
    else:
        await EditProducts.for_new_field.set()
        await call.message.answer('Отправьте новое значение')



async def set_new_value(message: types.message, state: FSMContext):
    user_data = await state.get_data()

    productid = user_data['articul']
    field = user_data['field']

    new_value = message.text

    main_db.update_product_field(productid, field, new_value)

    await message.answer(f'Поле {field} успешно обновлено!\n'
                         f'Обновите список!')

    await state.finish()


async def set_new_photo(message: types.message, state: FSMContext):
    user_data = await state.get_data()
    productid = user_data['articul']

    photo_id = message.photo[-1].file_id

    main_db.update_product_field(productid, 'photo', photo_id)

    await message.answer("Фото успешно обновлено! \n"
                         "Обновите список!")
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands='send_edit')
    dp.register_callback_query_handler(send_all_products, Text(equals='edit_all'))
    dp.register_callback_query_handler(edit_product, Text(startswith='edit_'),
                                       state='*')
    dp.register_callback_query_handler(select_field_product,
                                       Text(startswith='field_'),
                                       state=EditProducts.for_field)
    dp.register_message_handler(set_new_value, state=EditProducts.for_new_field)
    dp.register_message_handler(set_new_photo, state=EditProducts.for_new_photo,
                                content_types='photo')