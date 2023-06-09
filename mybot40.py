from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import telebot
from telebot import types

# Здесь нужно вставить токен вашего бота
TOKEN = 'your_bot_token_here'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

def start(update, context):
    keyboard = [[InlineKeyboardButton("iPhone", callback_data='iphone'),
                 InlineKeyboardButton("iPad", callback_data='ipad')],
                [InlineKeyboardButton("MacBook", callback_data='macbook'),
                 InlineKeyboardButton("Apple Watch", callback_data='watch')],
                [InlineKeyboardButton("AirPods", callback_data='airpods')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)


def category(update, context):
    query = update.callback_query
    category = query.data
    if category == 'iphone':
        keyboard = [[InlineKeyboardButton("iPhone 13 Pro Max - 128GB ($1099)", callback_data='iphone_13_pro_max_128gb'),
                     InlineKeyboardButton("iPhone 13 Pro Max - 256GB ($1199)", callback_data='iphone_13_pro_max_256gb')],
                    [InlineKeyboardButton("iPhone 13 Pro - 128GB ($999)", callback_data='iphone_13_pro_128gb'),
                     InlineKeyboardButton("iPhone 13 Pro - 256GB ($1099)", callback_data='iphone_13_pro_256gb')],
                    [InlineKeyboardButton("Назад", callback_data='back')]]
    elif category == 'ipad':
        keyboard = [[InlineKeyboardButton("iPad Pro 12.9\" - 128GB ($1099)", callback_data='ipad_pro_12_9_128gb'),
                     InlineKeyboardButton("iPad Pro 12.9\" - 256GB ($1199)", callback_data='ipad_pro_12_9_256gb')],
                    [InlineKeyboardButton("iPad Pro 11\" - 128GB ($799)", callback_data='ipad_pro_11_128gb'),
                     InlineKeyboardButton("iPad Pro 11\" - 256GB ($899)", callback_data='ipad_pro_11_256gb')],
                    [InlineKeyboardButton("Назад", callback_data='back')]]
    elif category == 'macbook':
        keyboard = [[InlineKeyboardButton("MacBook Air - M1, 256GB ($999)", callback_data='macbook_air_m1_256gb'),
                     InlineKeyboardButton("MacBook Air - M1, 512GB ($1249)", callback_data='macbook_air_m1_512gb')],
                    [InlineKeyboardButton("MacBook Pro - M1, 256GB ($1299)", callback_data='macbook_pro_m1_256gb'),
                     InlineKeyboardButton("MacBook Pro - M1, 512GB ($1499)", def start(update, context):
    keyboard = [[InlineKeyboardButton("iPhone", callback_data='iphone'),
                 InlineKeyboardButton("iPad", callback_data='ipad')],
                [InlineKeyboardButton("MacBook", callback_data='macbook'),
                 InlineKeyboardButton("Apple Watch", callback_data='watch')],
                [InlineKeyboardButton("AirPods", callback_data='airpods')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)


def category(update, context):
    query = update.callback_query
    category = query.data
    if category == 'iphone':
        keyboard = [[InlineKeyboardButton("iPhone 13 Pro Max - 128GB ($1099)", callback_data='iphone_13_pro_max_128gb'),
                     InlineKeyboardButton("iPhone 13 Pro Max - 256GB ($1199)", callback_data='iphone_13_pro_max_256gb')],
                    [InlineKeyboardButton("iPhone 13 Pro - 128GB ($999)", callback_data='iphone_13_pro_128gb'),
                     InlineKeyboardButton("iPhone 13 Pro - 256GB ($1099)", callback_data='iphone_13_pro_256gb')],
                    [InlineKeyboardButton("Назад", callback_data='back')]]
    elif category == 'ipad':
        keyboard = [[InlineKeyboardButton("iPad Pro 12.9\" - 128GB ($1099)", callback_data='ipad_pro_12_9_128gb'),
                     InlineKeyboardButton("iPad Pro 12.9\" - 256GB ($1199)", callback_data='ipad_pro_12_9_256gb')],
                    [InlineKeyboardButton("iPad Pro 11\" - 128GB ($799)", callback_data='ipad_pro_11_128gb'),
                     InlineKeyboardButton("iPad Pro 11\" - 256GB ($899)", callback_data='ipad_pro_11_256gb')],
                    [InlineKeyboardButton("Назад", callback_data='back')]]
    elif category == 'macbook':
        keyboard = [[InlineKeyboardButton("MacBook Air - M1, 256GB ($999)", callback_data='macbook_air_m1_256gb'),
                     InlineKeyboardButton("MacBook Air - M1, 512GB ($1249)", callback_data='macbook_air_m1_512gb')],
                    [InlineKeyboardButton("MacBook Pro - M1, 256GB ($1299)", callback_data='macbook_pro_m1_256gb'),
                     InlineKeyboardButton("MacBook Pro - M1, 512GB ($1499)", callback_data='macbook_pro_m1_512gb')],
[InlineKeyboardButton("Назад", callback_data='back')]]
elif category == 'watch':
keyboard = [[InlineKeyboardButton("Apple Watch Series 7 GPS, 41mm ($399)", callback_data='watch_7_gps_41mm'),
InlineKeyboardButton("Apple Watch Series 7 GPS, 45mm ($429)", callback_data='watch_7_gps_45mm')],
[InlineKeyboardButton("Apple Watch Series 7 GPS + Cellular, 41mm ($499)", callback_data='watch_7_gps_cellular_41mm'),
InlineKeyboardButton("Apple Watch Series 7 GPS + Cellular, 45mm ($529)", callback_data='watch_7_gps_cellular_45mm')],
[InlineKeyboardButton("Назад", callback_data='back')]]
elif category == 'airpods':
keyboard = [[InlineKeyboardButton("AirPods (2nd generation) ($159)", callback_data='airpods_2nd_gen'),
InlineKeyboardButton("AirPods Pro ($249)", callback_data='airpods_pro')],
[InlineKeyboardButton("AirPods Max ($549)", callback_data='airpods_max')],
[InlineKeyboardButton("Назад", callback_data='back')]]

reply_markup = InlineKeyboardMarkup(keyboard)

query.edit_message_text('Выберите товар:', reply_markup=reply_markup)
def item(update, context):
query = update.callback_query
item = query.data

# Добавляем выбранный товар в список заказа
user = update.message.from_user
chat_id = update.message.chat_id

if 'iphone' in item:
    if '128gb' in item:
        context.user_data['order'].append({'item': 'iPhone 13 Pro Max', 'storage': '128GB', 'price': 1099})
    elif '256gb' in item:
        context.user_data['order'].append({'item': 'iPhone 13 Pro Max', 'storage': '256GB', 'price': 1199})
    elif '13_pro' in item:
        if '128gb' in item:
            context.user_data['order'].append({'item': 'iPhone 13 Pro', 'storage': '128GB', 'price': 999})
        elif '256gb' in item:
            context.user_data['order'].append({'item': 'iPhone 13 Pro', 'storage': '256GB', 'price': 1099})

elif 'ipad' in item:
    if '12_9' in item:
        if '128gb' in item:
            context.user_data['order'].append({'item': 'iPad Pro 12.9"', 'storage': '128GB', 'price': 1099})
        elif '256gb' in item:
            context.user_data['order'].append({'item': 'iPad Pro 12.9"', 'storage': '256GB', 'price': 1199})
    elif '11' in item:
        if '128gb' in item:
            context.user_data['order'].append({'item': 'iPad Pro 11"', 'storage': '128GB', 'price': 799})
        elif '256gb' in item:
            context.user_data['order'].append({'item': 'iPad Pro 11"', 'storage': '256GB', 'price': 899})

elif 'macbook' in item:
    if 'air' in item:
        if 'm1' in item:
            if '256gb' in item:
                context.user_data['order'].append({'item': 'iPad Pro 12.9"', 'storage': '128GB', 'price': 1099})
        elif '256gb' in item:
            context.user_data['order'].append({'item': 'iPad Pro 12.9"', 'storage': '256GB', 'price': 1199})

elif category == 'airpods':
    keyboard = [[InlineKeyboardButton("AirPods (2nd Gen) ($159)", callback_data='airpods_2nd_gen'),
                 InlineKeyboardButton("AirPods Pro ($249)", callback_data='airpods_pro')],
                [InlineKeyboardButton("Назад", callback_data='back')]]
reply_markup = InlineKeyboardMarkup(keyboard)
query.edit_message_text('Выберите товар:', reply_markup=reply_markup)

def product(update, context):
query = update.callback_query
product = query.data
price = None
if product == 'iphone_13_pro_max_128gb':
price = 1099
elif product == 'iphone_13_pro_max_256gb':
price = 1199
elif product == 'iphone_13_pro_128gb':
price = 999
elif product == 'iphone_13_pro_256gb':
price = 1099
elif product == 'ipad_pro_12_9_128gb':
price = 1099
elif product == 'ipad_pro_12_9_256gb':
price = 1199
elif product == 'ipad_pro_11_128gb':
price = 799
elif product == 'ipad_pro_11_256gb':
price = 899
elif product == 'macbook_air_m1_256gb':
price = 999
elif product == 'macbook_air_m1_512gb':
price = 1249
elif product == 'macbook_pro_m1_256gb':
price = 1299
elif product == 'macbook_pro_m1_512gb':
price = 1499
elif product == 'airpods_2nd_gen':
price = 159
elif product == 'airpods_pro':
price = 249

if price is None:
    query.edit_message_text('Произошла ошибка. Попробуйте еще раз.')
    return

context.user_data['product'] = product
context.user_data['price'] = price

keyboard = [[InlineKeyboardButton("Оформить заказ", callback_data='order')],
            [InlineKeyboardButton("Назад", callback_data='back')]]
reply_markup = InlineKeyboardMarkup(keyboard)
query.edit_message_text('Выбран товар {} по цене ${}. Что дальше?'.format(product.replace('_', ' ').title(), price), reply_markup=reply_markup)

def confirm_order(update, context):
query = update.callback_query
query.edit_message_text('Ваш заказ принят на обработку.')

product = context.user_data.get('product')
price = context.user_data.get('price')

if product is None or price is None:
    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text='Ошибка при оформлении заказа.')
    return

message = 'Поступил новый заказ!\n\nТовар: {}\nЦена: ${}\n'.format(product.replace('_', ' ').title(), price)
context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)

def back(update, context):
query = update.callback_query
query.edit_message_text('Выберите категорию:')
start(update, context)

def main():
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))

dp.add_handler(CallbackQueryHandler(category, def back(update, context):
query = update.callback_query
query.edit_message_text('Выберите категорию:')
start(update, context)

def main():
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

less
Copy code
dp.add_handler(CommandHandler('start', start))

dp.add_handler(CallbackQueryHandler(category, context=context))
dp.add_handler(CallbackQueryHandler(back, pattern='back', context=context))
dp.add_handler(CallbackQueryHandler(add_to_cart, pattern=r'^add_to_cart_', context=context))
dp.add_handler(CommandHandler('cart', show_cart, context=context))
dp.add_handler(CommandHandler('checkout', checkout, pass_user_data=True, context=context))

updater.start_polling()

if name == 'main':
main()
