from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from Cofme.private.token import TOKEN
from Cofme.src.core import main, archivator
import shutil
import os

bot = Bot(token=TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

users = [737823430]
COMMANDS_LIST = "Available command list:\n" \
                "/start - get start work the bot.\n" \
                "/help - get the list of available commands.\n" \
                "/update - To update the table data.\n" \
                "/get - To get a table in xlsx format.\n" \
                "/put - Change the table to its own"


def check_id(message: types.Message):
    if message.chat.id not in users:
        message.answer(text=r"Sorry, you don't have access")


@dp.message_handler(commands=['help', 'start'])
async def help(message: types.Message):
    check_id(message)
    await message.answer(text=COMMANDS_LIST)


@dp.message_handler(commands='update')
async def update_data(message: types.Message):
    check_id(message)
    main.start()
    await message.answer(text='data updated')


@dp.message_handler(commands='get')
async def get_data(message: types.Message):
    check_id(message)
    await message.answer_document(open('../../private/m2023.xlsx', 'rb'))


class Form(StatesGroup):
    data = State()


@dp.message_handler(commands='put')
async def start(message: types.Message):
    check_id(message)
    await message.answer("I expect the file in the next message")
    await Form.data.set()


@dp.message_handler(content_types=['document'], state=Form.data)
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        try:
            file_id = message.document.file_id
            file = await bot.get_file(file_id)
            await bot.download_file(file.file_path, destination='cache/m2023.xlsx')
            archivator.screen()
            shutil.copy2('cache/m2023.xlsx', '../../private')
        except:
            await message.answer("Error occurred, data was not updated")
        else:
            await message.answer("All right, data was updated")
        finally:
            for i in os.listdir('cache'):
                os.remove(f"cache/{i}")
            await state.finish()


executor.start_polling(dp, skip_updates=True)
