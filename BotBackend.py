from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from fuzzywuzzy import fuzz
 
import BotConfig
import GetWeather as Parser

Last_msg = {}

bot = Bot(BotConfig.TOKEN)
dp = Dispatcher(bot)

button_get = KeyboardButton('Выбрать местоположение')
button_hi = KeyboardButton('Hi')
main_kb = ReplyKeyboardMarkup()
main_kb.add(button_get).add(button_hi)

def BotStart():
	@dp.message_handler(commands="start")
	async def cmd_start(message: types.Message):
    		#await message.reply("Hello!", reply_markup=main_kb)
    		 await bot.send_message(message.from_user.id, "Hi!", reply_markup=main_kb)

def BotMessage():
	@dp.message_handler()
	async def echo_message(msg: types.Message):
		if msg.text == "Выбрать местоположение":
			await bot.send_message(msg.from_user.id, "Введите страну")
			Last_msg[UserId(msg)] = "Введите страну"
		else:
			if Last_msg[UserId(msg)] == "Введите страну":
				print("ok")
				Last_msg[UserId(msg)] = " "
			else:
				await bot.send_message(msg.from_user.id, "Excuse me, I don't understand")
  
def BotPolling():
	executor.start_polling(dp, skip_updates=True)
	
def UserId(msg):
	return(msg.chat.id)
	
	
