#А/В калькулятор

import tkinter as tk

def do_close():
    root.destroy()

# главное окно программы
root = tk.Tk()
root.geometry('280x300')
root.title('A/B калькулятор')

# Creating hadler lable
lblTitle = tk.Label(text='A/B Калькулятор', font=('Bahnschrift', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=20)

# Creating hadler lable for control group
lblTitle1 = tk.Label(text='Контрольная группа', font=('Bahnschrift', 13, 'bold'), fg='#0066ff')
lblTitle1.place(x=45, y=50)

# Adding input labels for control group
lblVisitors1= tk.Label(text='Посетители', font=('Bahnschrift', 10, 'bold'))
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font=('Bahnschrift', 10, 'bold'))
entVisitors1.place(x=115, y=85, width=90, height=20)

lblConversions1= tk.Label(text='Конверсия', font=('Bahnschrift', 10, 'bold'))
lblConversions1.place(x=25, y=115)

entonversions1 = tk.Entry(font=('Bahnschrift', 12, 'bold'))
entonversions1.place(x=115, y=115, width=90, height=20)

# Creating hadler lable for test group
lblTitle2 = tk.Label(text='Тестовая группа', font=('Bahnschrift', 13, 'bold'), fg='#008800')
lblTitle2.place(x=55, y=140)

# Adding input labels for test group
lblVisitors2= tk.Label(text='Посетители', font=('Bahnschrift', 10, 'bold'))
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font=('Bahnschrift', 10, 'bold'))
entVisitors2.place(x=115, y=175, width=90, height=20)

lblConversions2= tk.Label(text='Конверсия', font=('Bahnschrift', 10, 'bold'))
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font=('Bahnschrift', 10, 'bold'))
entConversions2.place(x=115, y=205, width=90, height=20)

# Creating knob to calculate
btnProccess = tk.Button(text='Рассчитать', font=('Bahnschrift', 12, 'bold'))
btnProccess.place(x=25, y=250, width=110, height=30)

#3
# Creating knob to close
btnQuit = tk.Button(text='Выйти', font=('Bahnschrift', 12, 'bold'), command= do_close)
btnQuit.place(x=160, y=250, width=90, height=30)








# запуск цикла mainloop()
root.mainloop()