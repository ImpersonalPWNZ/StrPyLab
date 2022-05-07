import tkinter as tk
from tkinter import *
from tkinter import messagebox
import xmlrpc.client
def StrLen(str):
    messagebox.showinfo("Длина строки",f"Длина строки = {proxy.StrLen(str)}")
def SubstrInStr(str,sub):
    messagebox.showinfo("Подсчет подстроки", f"Подстрока {sub} встречается в строке {str} {proxy.SubstrInStr(str,sub)} раз")
def WordCountInStr(str):
    messagebox.showinfo("Количество слов", f"Количество слов в строке {proxy.WordCountInStr(str)} = {len(str.split())}")
def StrType(str):
    messagebox.showinfo("Тип строки", f"{proxy.StrType(str)}")
def StrFormat(str):
    messagebox.showinfo("Формат строки", f"{proxy.StrFormat(str)}")


if __name__ == '__main__':
    window = tk.Tk()
    proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
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


