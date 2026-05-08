from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧠 Детектив"),
         KeyboardButton(text="📊 Факты")],
    ],
    resize_keyboard=True
)

random_fact_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Случайный факт", callback_data="random_fact")]
    ]
) 