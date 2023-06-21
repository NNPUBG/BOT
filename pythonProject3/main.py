import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
ikb1 = ReplyKeyboardMarkup(row_width=1)
ib1 = KeyboardButton(text='/1M')
ib2 = KeyboardButton(text='/2M')
ib4 = KeyboardButton(text='/4M')
ikb1.add(ib1, ib2, ib4)

ikb4 = ReplyKeyboardMarkup(row_width=1)
iba = KeyboardButton(text='/start')
ikb4.add(iba)
@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                        text='МЕНЮ: /1M - грошова допомога автору, /2M - інформація про автора,  /4M - телеграм канал автора',
                        reply_markup=ikb1)

ikb2 = ReplyKeyboardMarkup(row_width=1)
ib1S = KeyboardButton(text='/1S')
ib2S = KeyboardButton(text='/2S')
ib3S = KeyboardButton(text='/3S')
ib4S = KeyboardButton(text='/4S')
ib5S = KeyboardButton(text='/5S')
ikb2.add(ib5S, ib4S, ib3S, ib2S, ib1, iba)

PRICE1 = types.LabeledPrice(label="Підтримка автора", amount=1 * 100)
PRICE2 = types.LabeledPrice(label="Підтримка автора", amount=10 * 100)
PRICE3 = types.LabeledPrice(label="Підтримка автора", amount=20 * 100)
PRICE4 = types.LabeledPrice(label="Підтримка автора", amount=100 * 100)
PRICE5 = types.LabeledPrice(label="Підтримка автора", amount=500 * 100)

@dp.message_handler(commands=['1M'])
async def ww(message: types.Message):
   await bot.send_message(chat_id=message.from_user.id,
                        text='Розмір підтримки /1S - надіслати 1 грн, /2S - надіслати 10 грн, /3S - надіслати 20 грн , /4S - надіслати 100 грн, /5S - надіслати 500 грн, /start - повернутися назад',
                        reply_markup=ikb2)



@dp.message_handler(commands=['1S'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'Квитанція':
        await bot.send_message(message.chat.id, "Квитанція на оплату")

    await bot.send_invoice(message.chat.id,
                           title="Квитанція",
                           description="Квитанція на оплату",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="uah",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE1],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")

@dp.message_handler(commands=['2S'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'Квитанція':
        await bot.send_message(message.chat.id, "Квитанція на оплату")

    await bot.send_invoice(message.chat.id,
                           title="Квитанція",
                           description="Квитанція на оплату",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="uah",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE2],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")

@dp.message_handler(commands=['3S'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'Квитанція':
        await bot.send_message(message.chat.id, "Квитанція на оплату")

    await bot.send_invoice(message.chat.id,
                           title="Квитанція",
                           description="Квитанція на оплату",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="uah",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE3],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")

@dp.message_handler(commands=['4S'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'Квитанція':
        await bot.send_message(message.chat.id,
                               "Квитанція на оплату",
                               reply_markup=ikb4)


    await bot.send_invoice(message.chat.id,
                           title="Квитанція",
                           description="Квитанція на оплату",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="uah",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE4],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")

@dp.message_handler(commands=['5S'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'Квитанція':
        await bot.send_message(message.chat.id, "Квитанція на оплату")

    await bot.send_invoice(message.chat.id,
                           title="Квитанція",
                           description="Квитанція на оплату",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="uah",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE5],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")
# price

# buy



# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платіж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} пройшов успішно!!!")



@dp.message_handler(commands=['2M'])
async def info(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Привіт я NNPUBG і ось основна інформація про мене: Ім'я Остап вік 13 місто Київ. нажміть на кнопку щоб повернутися до меню",
                           reply_markup=ikb4)





















































ikb3 = InlineKeyboardMarkup(row_width=1)
dr = InlineKeyboardButton(text='Телеграм канал',
                          url='https://t.me/ttnnpubg')
ikb3.add(dr)
@dp.message_handler(commands=['4M'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                        text='Телеграм канал',
                        reply_markup=ikb3)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)