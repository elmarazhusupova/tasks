import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint as pp

tg_bot_token = '5076215794:AAHTz0A8kIxKMGEnqY1dhJPUCUd-413u6WE'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


r = requests.get('https://rickandmortyapi.com/api/character')
data = r.json()
characters_raw = data['results']
characters = dict()

for values in characters_raw:
    characters[values['name']] = values


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("hello! enter character name")


@dp.message_handler()
async def get_info_about_character(message: types.Message):
    try:
        character = characters[message.text]
        await message.reply(f"{character['name']} {character['gender']} {character['status']} {character['species']}")
    except:
        print("Error")

executor.start_polling(dp)