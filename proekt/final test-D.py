from tkinter import*
import tkinter
import random
from tkinter import messagebox

temp = 61
i = 0


def knopka(event, obj):
    enter.insert(index=len(enter.get()), string=obj)


def exit():  # функция закрывающая игру
    game.destroy()


def reset():
    global i

    otvet = enter.get()
    enter.delete(first=0, last=END)
    a = answer
    if str(a) == otvet:
        i = i + 100
        ochki.configure(text=str(i))
    ochki.configure(text=str(i))
    if temp != 0:  # пока таймер не истёк мы играем
        questionsGeneration()
        print(arith, answer)
        primer.configure(text=str(question))




def questionsGeneration():  # функция генерирует примеры
    global question, answer, number1, number2, arith
    number1, number2, arith, question, answer = 0, 0, '', '', 0
    arithmetic = [' + ', ' - ']
    number1 = random.choice(range(20))
    number2 = random.choice(range(20))
    arith = random.choice(arithmetic)
    question = str(number1) + arith + str(number2) + ' = '

    if arith == ' + ':
        answer = number1 + number2
    elif arith == ' - ':
        if number1 < number2:
            answer = number2 - number1
            question = str(number2) + arith + str(number1) + ' = '



def tick():
    global temp
    temp -= 1
    if temp > 0:
        game.after(1000, tick)
        sec.configure(text=str(temp))



def Game():  # функция которая запускает игру после нажатия на кнопку ИГРАТЬ
    # забываем расположение кнопок меню и название игры
    nvn.place_forget()
    bgame.place_forget()
    bnastr.place_forget()
    bexit.place_forget()

    # пример и поле ввода
    primer.place(x=20, y=140)
    enter.place(x=20, y=250)

    # размещаем кнопки для игры

    b1.place(x=6, y=555, width=90)
    b2.place(x=98, y=555, width=90)
    b3.place(x=190, y=555, width=90)
    b0.place(x=282, y=555, width=90)
    b4.place(x=6, y=448, width=90)
    b5.place(x=98, y=448, width=90)
    b6.place(x=190, y=448, width=90)
    b7.place(x=6, y=341, width=90)
    b8.place(x=98, y=341, width=90)
    b9.place(x=190, y=341, width=90)
    bok.place(x=282, y=341, width=90, height=212)

    # размещаяем строку состояния
    ochki.pack(side='top')
    lab.place(x=2, y=0)
    sec.place(x=330, y=0)

    # Таймер
    print("test")
    tick()
    questionsGeneration()  # вызываем для начала игры
    primer.configure(text=str(question))




game = Tk()  # создаём окно меню
game.geometry("376x667")  # задаём размер окна
game.title("УСТНЫЙ СЧЁТ")  # дали название окну


# ВИДЖЕТЫ ТЕКСТ
nvn = Label(game, fg='black', text='УСТНЫЙ СЧЁТ', font='Arial 30')  # навание игры в меню
lab = Label(game, text='Очки', fg='black', font='Arial 25')  # текст Очки
sec = Label(game, fg='black', text='60', font='Arial 25')  # таёмер
ochki = Label(game, text='0', fg='black', font='ComicSansMS 25')  # очки
primer = Label(game, text='',fg='black', font='Arial 50')
molodec = Label(game, text='Молодец!', fg='black', font='Arial 30 ')
enter = Entry(game, width=22,bd=1, font= "Arial 20")

# КНОПКИ МЕНЮ
bgame = Button(game, text='Играть', bg='white', fg='black', font='Arial 24', command=Game)  # кнопка "Играть"
bnastr = Button(game, text='Настройки', bg='white', fg='black', font='Arial 24')  # кнопка "Настройки"
bexit = Button(game, text='Выход', bg='white', fg='black', font='Arial 24', command=exit)  # кнопка "Выход"

# КНОПКИ С ЦИФРАМИ В ИГРЕ
b0 = Button(game, text='0', font='Arial 40')
b1 = Button(game, text='1', font='Arial 40')
b2 = Button(game, text='2', font='Arial 40')
b3 = Button(game, text='3', font='Arial 40')
b4 = Button(game, text='4', font='Arial 40')
b5 = Button(game, text='5', font='Arial 40')
b6 = Button(game, text='6', font='Arial 40')
b7 = Button(game, text='7', font='Arial 40')
b8 = Button(game, text='8', font='Arial 40')
b9 = Button(game, text='9', font='Arial 40')
b0.bind("<1>", lambda event,obj="0": knopka(event, obj))
b1.bind("<1>", lambda event,obj="1": knopka(event, obj))
b2.bind("<1>", lambda event,obj="2": knopka(event, obj))
b3.bind("<1>", lambda event,obj="3": knopka(event, obj))
b4.bind("<1>", lambda event,obj="4": knopka(event, obj))
b5.bind("<1>", lambda event,obj="5": knopka(event, obj))
b6.bind("<1>", lambda event,obj="6": knopka(event, obj))
b7.bind("<1>", lambda event,obj="7": knopka(event, obj))
b8.bind("<1>", lambda event,obj="8": knopka(event, obj))
b9.bind("<1>", lambda event,obj="9": knopka(event, obj))
bok = Button(game, text='OK',
             bg="green",
             fg="white",
             font='Arial 30',
             activebackground='darkgreen',
             activeforeground='white',
             command=reset)

# ОТОБРАЖЕНИЕ В МЕНЮ
nvn.place(x=45, y=100, width=300)  # отображаем название на экране
bgame.place(x=90, y=200, width=200)  # отображаем кнопку ИГРАТЬ на экране
bnastr.place(x=90, y=300, width=200)  # отображаем кнопку НАСТРОЙКИ на экране
bexit.place(x=90, y=400, width=200)  # отображаем кнопку ВЫХОД на экране




game.mainloop()  # зацикливаем


