from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command

router = Router()

@router.callback_query()
async def show_mess(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Рецепт", callback_data="get_recipe")
    builder.button(text="Анекдот", callback_data="get_joke")
    builder.button(text="Погода", callback_data="get_weather")

    await message.answer("Выберете: ", reply_markup=builder.as_markup())

@router.callback_query()
async def hendle_button(callback: types.CallbackQuery):
    data = callback.data
