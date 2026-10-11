import os
from dotenv import load_dotenv 
from vkbottle import Bot 
from vkbottle.bot import Message
import random

load_dotenv()

TOKEN = os.getenv("VK_TOKEN")

bot = Bot(token = TOKEN)

@bot.on.message(text='Привет')
async def greetings(message: Message):
    await message.answer('Привет! Все работает правильно!')


@bot.on.message(text='Пока')
async def goodbuy(message: Message):
    await message.answer('Ладно пока!')

@bot.on.message(text='Кубик')
async def roll(message: Message):
    r_num = random.randint(1,6)
    await message.answer(f'Кубик показал {r_num}')

@bot.on.message()
async def handle_message(message:Message):
    responce = ['да', 'нет', 'скорее всего']
    word = random.choice(responce)
    await message.answer(word)


bot.run()