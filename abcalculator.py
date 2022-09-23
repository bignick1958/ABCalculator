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

# Creating knob to calculate
btnProccess = tk.Button(text='Рассчитать', font=('Bahnschrift', 12, 'bold'))
btnProccess.place(x=25, y=250, width=110, height=30)

#3
# Creating knob to close
btnQuit = tk.Button(text='Выйти', font=('Bahnschrift', 12, 'bold'), command= do_close)
btnQuit.place(x=160, y=250, width=90, height=30)








# запуск цикла mainloop()
root.mainloop()