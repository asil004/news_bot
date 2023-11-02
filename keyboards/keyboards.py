from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton


def menu():
    keyboard = KeyboardBuilder(KeyboardButton)
    keyboard.add(
        *[
            KeyboardButton(text='Latest news'),
            KeyboardButton(text='Search'),
            KeyboardButton(text='About us')
        ]
    )
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)
