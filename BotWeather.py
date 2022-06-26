import GetWeather as parser

import BotBackend


URL0 = 'https://rp5.ru'
URL1 = '/Погода_в_мире'
URL = URL0 + URL1

BotBackend.BotStart()

BotBackend.BotTest()

BotBackend.BotMessage()
    		
BotBackend.BotPolling()

#@dp.callback_query_handler(func=lambda c: c.data == 'button1')
#async def process_callback_button1(callback_query: types.CallbackQuery):
#    await bot.answer_callback_query(callback_query.id)
#    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


#countries_list, countries_links = parser.parse(URL) 
#print(countries_links)
