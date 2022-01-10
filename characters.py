import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


tg_bot_token = ''
rick_and_morty = ''

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Choose a character to get information")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f"""https://rickandmortyapi.com/api/character  """)
        data = r.json
        character = data['name']
        status = data['main']['status']
        species = data['main']['species']
        gender = data['main']['gender']

        await message.reply(f"""
        Name = {character},
        Status = {status},
        Species = {species},
        Gender = {gender}
        """)
    except:
        print("Error")
