from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from fuzzywuzzy import fuzz
 
import BotConfig
import GetWeather as Parser

URL0 = 'https://rp5.ru'
URL1 = '/Погода_в_мире'
URL = URL0 + URL1

Deep_id = {}

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
			Deep_id[UserId(msg)] = "Страна"
		else:
			if Deep_id[UserId(msg)] == "Страна":
				Url_reg = URL
				high, mid, countries, countries_links = FindDisp(msg, Url_reg)
				if high == []:
					await bot.send_message(msg.from_user.id, "Нет точных совпадений. Возможно, вы имели в виду что-то из:")
					for c in mid:
						await bot.send_message(msg.from_user.id, c)
					if mid == []:
						await bot.send_message(msg.from_user.id, "Нет даже примерных совпадений, хм")
				else:
					Deep_id[UserId(msg)] = "Регион" + countries_links[countries.index(high[-1])]
					
					await bot.send_message(msg.from_user.id, "Страна найдена, введите регион")
			
			elif "Регион" in Deep_id[UserId(msg)]:
				Url_reg = URL0 + Deep_id[UserId(msg)].replace("Регион","")
				print(Url_reg)
				if not (URL0+"/") in Url_reg:
					Url_reg = Url_reg.replace(URL0, URL0+"/")
				countries, countries_links = Parser.parse(Url_reg)
				high = []
				mid = []
				text = msg.text
				for country in countries:
					r = fuzz.ratio(country, text)
					if r == 100:
						high.append(country)
					if r > 50:
						mid.append(country)
				if high == []:
					await bot.send_message(msg.from_user.id, "Нет точных совпадений. Возможно, вы имели в виду что-то из:")
					for c in mid:
						await bot.send_message(msg.from_user.id, c)
					if mid == []:
						await bot.send_message(msg.from_user.id, "Нет даже примерных совпадений, хм")
				else:
					
					await bot.send_message(msg.from_user.id, "Регион найден, введите населённый пункт")
					Deep_id[UserId(msg)] = "Город" + countries_links[countries.index(high[-1])]
			
			elif "Город" in Deep_id[UserId(msg)]:
				Url_reg = URL0 + Deep_id[UserId(msg)].replace("Город","")
				print(Url_reg)
				if not (URL0+"/") in Url_reg:
					Url_reg = Url_reg.replace(URL0, URL0+"/")
				countries, countries_links = Parser.parse(Url_reg)
				high = []
				mid = []
				text = msg.text
				for country in countries:
					r = fuzz.ratio(country, text)
					if r == 100:
						high.append(country)
					if r > 50:
						mid.append(country)
				if high == []:
					await bot.send_message(msg.from_user.id, "Нет точных совпадений. Возможно, вы имели в виду что-то из:")
					for c in mid:
						await bot.send_message(msg.from_user.id, c)
					if mid == []:
						await bot.send_message(msg.from_user.id, "Нет даже примерных совпадений, хм")
				else:
					
					await bot.send_message(msg.from_user.id, "Населённый пункт найден, ура!")
					Deep_id[UserId(msg)] = "Точка" + countries_links[countries.index(high[-1])]
					
			elif "Точка" in Deep_id[UserId(msg)]:
				Url_reg = URL0 + Deep_id[UserId(msg)].replace("Точка","")
				print(Url_reg)
				
			else:
				await bot.send_message(msg.from_user.id, "Excuse me, I don't understand")
  
def BotPolling():
	executor.start_polling(dp, skip_updates=True)
	
def UserId(msg):
	return(msg.chat.id)
	
def FindDisp(msg, Url_reg):
	if not (URL0+"/") in Url_reg:
		Url_reg = Url_reg.replace(URL0, URL0+"/")
	countries, countries_links = Parser.parse(Url_reg)
	high = []
	mid = []
	text = msg.text
	for country in countries:
		r = fuzz.ratio(country, text)
		if r == 100:
			high.append(country)
		if r > 50:
			mid.append(country)
	return(high, mid, countries, countries_links)
