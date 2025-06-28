from aiogram import Router, types

router = Router()

list_bad = ["сука", "бля", "блядь", "иди на хуй", "иди в пень", "лох"]

@router.message()
async def echo_message(message: types.Message):
    text = message.text.lower()

    if any(bad_world in text for bad_world in list_bad):
        await message.answer("Эй! Не ругайся")
    elif "привет" in text:
        await message.answer("Привет, че как?")
    else:
        await message.answer(f"{message.text}.")