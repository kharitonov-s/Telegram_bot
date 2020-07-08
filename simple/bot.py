import datetime

from telegram import Bot
from telegram import ParseMode
from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request

button_help = 'Помощь'

# 'callback_data' -- это то, что будет присылать ТГ при нажатии на каждую кнопку
# поэтому каждый идентификатор должен быть уникальным
CALLBACK_BUTTON1_LEFT = "callback_button1_left"
CALLBACK_BUTTON2_MID = "callback_button2_mid"
CALLBACK_BUTTON3_RIGHT = "callback_button3_right"

# надписи на кнопках
TITLES = {
    CALLBACK_BUTTON1_LEFT: "Мужской",
    CALLBACK_BUTTON2_MID: "Женский",
    CALLBACK_BUTTON3_RIGHT: "Не знаю",
}

def get_base_inline_keyboard():
    """ Получить клавиатуру для сообщений
        Эта клавиатура будет видна под каждым сообщением, где ее прикрепили"""
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_MID], callback_data=CALLBACK_BUTTON2_MID),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_RIGHT], callback_data=CALLBACK_BUTTON3_RIGHT),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

# обработка кнопок
def keyboard_callback_handler(bot: Bot, update: Update, context: CallbackContext, **kwargs):
    """Обработчки всех кнопок со ВСЕХ клавиатур
    """
    query = update.callback_query
    data = query.data
    now = datetime.datetime.now()

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == CALLBACK_BUTTON1_LEFT:
        context.user_data[GENDER] =
        query.edit_message_text(
            text='Введите свой возраст',
            parse_mode=ParseMode.MARKDOWN,
        )
        # Отправим новое сообщение при нажатии на кнопку
        bot.send_message(
            chat_id=chat_id,
            text="Новое сообщение\n\ncallback_query.data={}".format(data),
            reply_markup=get_base_inline_keyboard(),
        )
    elif data == CALLBACK_BUTTON2_MID:


# decorator (отлавливает ошибки)
def log_error(f):

    # функция, которую возвращает декоратор
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e
    return inner


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это помощь!',                 # выводит текст
        reply_markup=ReplyKeyboardRemove(), # ответное действие = (убирает кнопки)
    )
@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        # задается клавиатура (список списков).
        # Первый список - вертикальные ряды (кол-во вертикальных строк)
        # Второй список - кнопки в каждой горизонтальной строке
        keyboard=[
            [
                KeyboardButton(text=button_help),
            ],
            [
                KeyboardButton(text=button_help),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text='Привет, нажми кнопку ниже!',  # выодвит текст
        reply_markup=reply_markup,          # отетное действие = (выводит клавиатуру)
    )


    # print(x)
   # user = update.effective_user
   #  if user:
   #     name = user.first_name
   #  else: name = 'аноним'
   #
   #  text = update.effective_message.text
   #  reply_text = f'Привет, {name}!\n\n{text}'
   #
   #  bot.send_message(
   #      chat_id=update.effective_message.chat_id,
   #      text=reply_text,


def main():
    print('Start ')

    req = Request(
        connect_timeout=0.5,
    )
    bot = Bot(
        request=req,
        token="861509585:AAF4o3XNxc4ZrRZu1rtFacZoS2r_jwbE1p4",
        base_url="https://telegg.ru/orig/bot",
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))


    updater.start_polling()
    updater.idle()

    print('Finish')

if __name__ == '__main__':
    main()

