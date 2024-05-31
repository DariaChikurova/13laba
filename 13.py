import tkinter as tk
def zadanie1():
    def on_click(event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            except Exception as e:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
        elif text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, text)
    root = tk.Tk()
    root.title("Simple Calculator")
    entry = tk.Entry(root, width=40, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4)
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]
    row = 1
    col = 0
    for button_text in buttons:
        button = tk.Button(root, text=button_text, padx=20, pady=10)
        button.grid(row=row, column=col)
        button.bind("<Button-1>", on_click)
        col += 1
        if col > 3:
            col = 0
            row += 1
    root.mainloop()



from tkinter import Tk, Frame, Entry, Button, Label
import requests

# Функция для получения погоды
def zadanie2():
    city = cityField.get()
    key = '&key=YOUR_API_KEY'  # Замените 'ВАШ КЛЮЧ' на ваш API ключ от OpenWeatherMap
    url = 'https://places.googleapis.com/v1/places/GyuEmsRBfy61i59si'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}°C'

# Настройки главного окна
root = Tk()
root['bg'] = '#fafafa'
root.title('dostoprimechatelnosti')
root.geometry('300x250')
root.resizable(width=False, height=False)

# Создание фреймов
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создание текстового поля для ввода города
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

# Создание кнопки для получения погоды
btn = Button(frame_top, text='Посмотреть достопримечательность', command=zadanie2)
btn.pack()

# Создание текстовой надписи для отображения погоды
info = Label(frame_bottom, text='достопримечательная информация', bg='#ffb700', font=40)
info.pack()

# Запуск основного цикла
root.mainloop()


zadanie2()