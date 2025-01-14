from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage



from utils.env import BOT_TOKEN


import logging

logging.basicConfig(level=logging.INFO)

storege = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode='html')


dp = Dispatcher(bot, storage=storege)