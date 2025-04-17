import uuid
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon import texts
from services.process_excel import process_excel_file_data

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=texts.get("start_message"))


@router.message(F.document)
async def process_excel_file(message: Message):
    document = message.document

    if document.mime_type in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]:
        file = await message.bot.get_file(document.file_id)
        file_name = f"downloads/{str(uuid.uuid4())[:8]}_{document.file_name}"
        await message.bot.download_file(file.file_path, destination=file_name)

        data = process_excel_file_data(file_name, message)
        message_text = "\n".join([f"Title: {item[0]}\n Url: {item[1]}\n price: {item[2]}\n" for item in data[:10]])
        await message.answer(message_text)
    else:
        await message.answer("Пожалуйста отправьте Excel файл (расширения: xlsx, xls)")


@router.message()
async def process_any_other_command(message: Message):
    await message.answer("Нет такой команды! Нажмите /start")


# ПРОВЕРКА ФУНКЦИИ get_user_data
# @router.message(F.text == "get_data")
# async def process_get_data(message: Message):
#     data = get_user_data(message.from_user.id)
#     await message.answer(str(data))
