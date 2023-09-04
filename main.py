from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text



API_TOKEN = 'telegram API token'






# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	#keyboard
	keyboard = types.ReplyKeyboardMarkup()
	button_1 = types.KeyboardButton(text="Узнать погоду") # a button
	keyboard.add(button_1) # adding a button to keyboard
	await message.answer("Привет, я бот Григория Московского!", reply_markup = keyboard)



@dp.message_handler(Text(equals = "Узнать погоду"))
async def get_weather(message: types.Message):
	await message.answer('Введите сообщение: "Погода <город, в котором вы хотите узнать погоду>	"')


@dp.message_handler(lambda message: message.text and 'погода' in message.text.lower())
async def echo(message: types.Message):
	choosed_place = message.text[7:]
	from weather import get_temperature_at_place
	await message.answer("Погода в городе " + choosed_place + ": " + str(get_temperature_at_place(choosed_place)))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
