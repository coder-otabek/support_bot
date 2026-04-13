from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Qo'llab-quvvatlash")
        ],
        [
            KeyboardButton(text="🧑‍💻 Admin bilan bog'lanish")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
