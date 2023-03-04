from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from cofme.private.token import TOKEN
from cofme.project.mining_income_statistics import main, req, archivator

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users = [737823430]


def check_id(message: types.Message):
    if message.chat.id not in users:
        message.answer(text=r"Sorry, you don't have access")


@dp.message_handler(commands='start')
async def start(message: types.Message):
    check_id(message)
    await message.answer(text='start')


@dp.message_handler(commands='help')
async def help(message: types.Message):
    check_id(message)
    await message.answer(text='help')


# @dp.message_handler(commands='update')
# async def update_data(message: types.Message):
#     check_id(message)
#     main.start()
#     await message.answer(text='data updated')


executor.start_polling(dp, skip_updates=True)
