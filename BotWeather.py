import GetWeather as parser
import BotConfig

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

URL0 = 'https://rp5.ru'
URL1 = '/Погода_в_мире'
URL = URL0 + URL1

bot = Bot(BotConfig.TOKEN)
dp = Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')
my_kb = ReplyKeyboardMarkup()
my_kb.add(button_hi)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Hello!", reply_markup=my_kb)

@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

#@dp.callback_query_handler(func=lambda c: c.data == 'button1')
#async def process_callback_button1(callback_query: types.CallbackQuery):
#    await bot.answer_callback_query(callback_query.id)
#    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

executor.start_polling(dp, skip_updates=True)

#countries_list, countries_links = parser.parse(URL) 
#print(countries_links)
