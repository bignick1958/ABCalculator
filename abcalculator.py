# А/В калькулятор
import math
import tkinter as tk
from tkinter import messagebox as mb
import os
import math


def do_close():
    root.destroy()


# num formatting funcction
def num_percent(num):
    return "{:.2f}".format(num * 100).rjust(10) + '%'


# reading data from a lables
def do_processing():
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())

    # entry labels control
    if n1 <= 0 or n2 <= 0:
        mb.showerror(title='Ошибка', message='Неверное количество посетителей')
        return

    popup_window(n1, c1, n2, c2)


def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry('500x500')
    window['bg'] = '#8fffff'
    window.title('А/В Результат')

    # adding text output window
    txt_output = tk.Text(window, font=('Courier New', 10, 'bold'))
    txt_output.place(x=15, y=115, width=470, height=300)

    # adding headler's
    txt_output.insert(tk.END, '                          Контрольная      Тестовая' + os.linesep)
    txt_output.insert(tk.END, '                          группа           группа  ' + os.linesep)
    txt_output.insert(tk.END, '__________________________________________________________' + os.linesep)

    # adding outpot for conversion and standart deviation
    p1 = c1 / n1
    p2 = c2 / n2
    txt_output.insert(tk.END, 'Конверсия             ' + num_percent(p1)
                      + '     ' + num_percent(p2) + os.linesep)
    sigma1 = math.sqrt(p1 * (1 - p1) / n1)
    sigma2 = math.sqrt(p2 * (1 - p2) / n2)
    txt_output.insert(tk.END, 'Стандартное отклонение' + num_percent(sigma1)
                      + '     ' + num_percent(sigma2) + os.linesep)
    txt_output.insert(tk.END, '                                               ' + os.linesep)

    # widow closing knob
    btn_close_popup = tk.Button(window, text='Закрыть', font=('Bahnschrift', 12, 'bold'), command=window.destroy)
    btn_close_popup.place(x=390, y=450, width=90, height=30)

    # fous in opend window
    window.focus_set()


# главное окно программы
root = tk.Tk()
root.geometry('280x300')
root['bg'] = '#C5C6C6'
root.title('A/B калькулятор')

# Creating hadler lable
lblTitle = tk.Label(text='A/B Калькулятор', font=('Bahnschrift', 16, 'bold'), fg='#0000cc', bg='#C5C6C6')
lblTitle.place(x=55, y=20)

# Creating hadler lable for control group
lblTitle1 = tk.Label(text='Контрольная группа', font=('Bahnschrift', 13, 'bold'), fg='#0066ff', bg='#C5C6C6')
lblTitle1.place(x=25, y=50)

# Adding input labels for control group
lblVisitors1 = tk.Label(text='Посетители', font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6')
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6', justify='center')
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END, '255')

lblConversions1 = tk.Label(text='Конверсия', font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6')
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6', justify='center')
entConversions1.place(x=115, y=115, width=90, height=20)
entConversions1.insert(tk.END, '26')

# Creating hadler lable for test group
lblTitle2 = tk.Label(text='Тестовая группа', font=('Bahnschrift', 13, 'bold'), fg='#008800', bg='#C5C6C6')
lblTitle2.place(x=25, y=140)

# Adding input labels for test group
lblVisitors2 = tk.Label(text='Посетители', font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6')
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6', justify='center')
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END, '235')

lblConversions2 = tk.Label(text='Конверсия', font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6')
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font=('Bahnschrift', 10, 'bold'), bg='#C5C6C6', justify='center')
entConversions2.place(x=115, y=205, width=90, height=20)
entConversions2.insert(tk.END, '18')
# Creating knob to calculate
btnProccess = tk.Button(text='Рассчитать', font=('Bahnschrift', 12, 'bold'), command=do_processing)
btnProccess.place(x=25, y=250, width=110, height=30)

# 3
# Creating knob to close
btnQuit = tk.Button(text='Выйти', font=('Bahnschrift', 12, 'bold'), command=do_close)
btnQuit.place(x=160, y=250, width=90, height=30)

# запуск цикла mainloop()
root.mainloop()
