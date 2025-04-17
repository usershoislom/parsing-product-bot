from aiogram.types import Message
import pandas as pd

from database.crud import save_excel_data, save_user_data
from services.process_xpath import get_price_from_xpath

def process_excel_file_data(filename: str, message: Message):
    user_id = message.from_user.id
    save_user_data(user_id)
    df = pd.read_excel(filename, engine="openpyxl")

    data = []
    for index, row in df.iterrows():
        title = row["title"]
        url = row["url"]
        xpath = row["xpath"]

        price = get_price_from_xpath(url, xpath)
        save_excel_data(user_id, title, url, xpath, price)

        data.append((title, url, price))

    return data
