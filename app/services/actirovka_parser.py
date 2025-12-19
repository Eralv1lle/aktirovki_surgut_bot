import requests
from bs4 import BeautifulSoup as BS


def get_actirovka_info():
    r = requests.get("https://sitv.ru/actirovka/")
    bs = BS(r.text, "html.parser")
    actirovka = bs.find(class_="activ")
    dt = actirovka.find_all("h3")[0]
    shifts_and_messages = actirovka.find_all(["h2", "p"])

    a = shifts_and_messages[::2]
    b = shifts_and_messages[1::2]

    shifts_and_messages = list(zip(a, b))

    text = f"<b>{dt.text}</b>\n\n"

    for shift, message in shifts_and_messages:
        text += f"<u><i>{shift.text}</i></u>\n{message.text}\n\n"

    text += "<i>Данные взяты с сайта sitv: https://sitv.ru/</i>"

    return text
