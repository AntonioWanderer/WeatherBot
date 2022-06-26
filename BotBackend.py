from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
import BotConfig

bot = Bot(BotConfig.TOKEN)
dp = Dispatcher(bot)

button_get = KeyboardButton('Дай список стран')
main_kb = ReplyKeyboardMarkup()
main_kb.add(button_get)

def BotStart():
	@dp.message_handler(commands="start")
	async def cmd_start(message: types.Message):
    		await message.reply("Hello!", reply_markup=main_kb)

def BotTest():
	@dp.message_handler(commands="test1")
	async def cmd_test1(message: types.Message):
    		await message.reply("Test 1")

def BotMessage():
	@dp.message_handler()
	async def echo_message(msg: types.Message):
    		await bot.send_message(msg.from_user.id, msg.text)
    		
def BotPolling():
	executor.start_polling(dp, skip_updates=True)
