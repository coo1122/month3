from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import main_db

class FSM_shop(StatesGroup):
    name_product = State()
    size = State()
    category = State()
    price = State()
    productid = State()
    infoproduct = State()
    collection = State()
    product_photo = State()
    submit = State()


async def start_fsm_shop(message: types.Message):
    await FSM_shop.name_product.set()
    await message.answer('Модель одежды:')


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await FSM_shop.next()
    await message.answer('Размер одежды:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_shop.next()
    await message.answer('Категория одежды?')



async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text


    await FSM_shop.next()
    await message.answer('Цена одежды:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text


    await FSM_shop.next()
    await message.answer('ID товара:')

async def load_productid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['productid'] = message.text


    await FSM_shop.next()
    await message.answer('INFO товара:')


async def load_infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text


        await FSM_shop.next()
        await message.answer('Коллекция товара:')


async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text


    await FSM_shop.next()
    await message.answer('Фото одежды:')


async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id


    await FSM_shop.submit.set()
    await message.answer('Верны ли данные?')
    await message.answer_photo(photo=data['product_photo'],
                               caption=f'Название моделм - {data["name_product"]}\n'
                                       f'Размер - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Стоимость - {data["price"]}\n'
                                       f'ID товара - {data["productid"]}\n'
                                       f'INFO товара - {data["infoproduct"]}\n'
                                       f'Коллекция товара - {data["collection"]}\n'
                               )

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:

            await main_db.sql_insert_store(
                name_product=data['name_product'],
                size=data['size'],
                price=data['price'],
                photo=data['product_photo'],
                productid=data['productid']
            )

            await main_db.sql_insert_products_details(
                productid=data['productid'],
                category=data['category'],
                infoproduct=data['infoproduct']
            )

            await main_db.sql_insert_collection_products(
                productid=data['productid'],
                collection=data['collection']
            )


            await message.answer('Ваши данные сохранены')

        await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_shop, commands=['shop'])
    dp.register_message_handler(load_name_product, state=FSM_shop.name_product)
    dp.register_message_handler(load_size, state=FSM_shop.size)
    dp.register_message_handler(load_category, state=FSM_shop.category)
    dp.register_message_handler(load_price, state=FSM_shop.price)
    dp.register_message_handler(load_productid, state=FSM_shop.productid)
    dp.register_message_handler(load_infoproduct, state=FSM_shop.infoproduct)
    dp.register_message_handler(load_collection, state=FSM_shop.collection)
    dp.register_message_handler(load_product_photo, state=FSM_shop.product_photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_shop.submit)