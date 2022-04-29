import tkinter as tk
from tkinter import *
from tkinter import messagebox
def StrLen(str):
    messagebox.showinfo("Длина строки",f"Длина строки = {len(str)}")
def SubstrInStr(str,sub):
    messagebox.showinfo("Подсчет подстроки", f"Подстрока {sub} встречается в строке {str} {str.count(sub)} раз")
def WordCountInStr(str):
    messagebox.showinfo("Количество слов", f"Количество слов в строке {str} = {len(str.split())}")
def StrType(str):
    str = str.replace(" ","")
    if str.isdigit():
        res = "В строке содержатся только цифры"
    elif str.isalpha():
        res = "В строке содержатся только буквы"
    elif str.isalnum():
        res = "В строке содержатся буквы и цифры"
    elif str =="":
        res = "Строка пустая"
    else:
        res = "В строке содержатся специальные символы"
    messagebox.showinfo("Тип строки", f"{res}")
def StrFormat(str):
    if str.isupper():
        res = "Только заглавные символы"
    elif str.islower():
        res = "Только строчные символы"
    else:
        res = "И заглавные и строчные символы"
    return messagebox.showinfo("Формат строки", f"{res}")


if __name__ == '__main__':
    window = tk.Tk()

    MainLabel = Label(text="Введите строку")
    StrEntry = Entry()
    SubLabel = Label(text="Введите подстроку")
    Sub = Entry()
    btn_len = Button(master=window, text="Длина строки", command=lambda: StrLen(StrEntry.get()))
    btn_substr = Button(master=window, text="Подсчет подстрок в строке", command=lambda: SubstrInStr(StrEntry.get(),Sub.get()))
    btn_word = Button(master=window, text="Количество слов в строке", command=lambda: WordCountInStr(StrEntry.get()))
    btn_type = Button(master=window, text="Тип строки", command=lambda: StrType(StrEntry.get()))
    btn_format = Button(master=window, text="Формат строки", command=lambda: StrFormat(StrEntry.get()))
    MainLabel.pack()
    StrEntry.pack()
    SubLabel.pack()
    Sub.pack()
    btn_len.pack()
    btn_substr.pack()
    btn_word.pack()
    btn_type.pack()
    btn_format.pack()
    window.mainloop()


