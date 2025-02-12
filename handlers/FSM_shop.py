from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_shop(StatesGroup):
    clothing_model = State()
    size = State()
    category = State()
    price = State()
    product_photo = State()
    submit=State()


async def start_fsm_shop(message: types.Message):
    await FSM_shop.clothing_model.set()
    await message.answer('Модель одежды:')


async def load_clothing_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['clothing_model'] = message.text

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
    await message.answer('Фото одежды:')


async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id


    await FSM_shop.next()
    await message.answer('Верны ли данные?')
    await message.answer_photo(photo=data['product_photo'],
                               caption=f'Название модели - {data["clothing_model"]}\n'
                                       f'Размер - {data["size"]}\n'
                                       f'Категория - {data["category"]}\n'
                                       f'Стоимость - {data["price"]}\n')

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await message.answer('Ваши данные сохранены')

        await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_shop, commands=['shop'])
    dp.register_message_handler(load_clothing_model, state=FSM_shop.clothing_model)
    dp.register_message_handler(load_size, state=FSM_shop.size)
    dp.register_message_handler(load_category, state=FSM_shop.category)
    dp.register_message_handler(load_price, state=FSM_shop.price)
    dp.register_message_handler(load_product_photo, state=FSM_shop.product_photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_shop.submit)