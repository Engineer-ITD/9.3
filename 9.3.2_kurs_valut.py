import requests, json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    pass

window = Tk()
window.title('КУрс обмена валют')
window.geometry('360x180')
Label(text='Введите код валюты').pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack()

window.mainloop()
result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)
p.pprint(data)