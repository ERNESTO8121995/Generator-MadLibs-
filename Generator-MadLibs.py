from tkinter import *


def w1():
    def w2():
        global word1

        def w3():
            global word2

            def w4():
                global word3

                def w5():
                    global word4

                    def w6():
                        global word5

                        def w7():
                            global word6

                            def final():
                                global word7
                                window.geometry('1100x550')
                                word7 = txt6.get()
                                label.place(x=-10, y=50)
                                label.config(
                                    text=f'Пациент, посмотрите на эту {word1}, вы видите это?\n- Да, но что это?\n - Это злокачественная {word2} внутри вашего организма,\n она растёт и в скором времени, станет слишком {word3},\n боюсь, мы ничего не можем сделать...\n - Но как, Доктор {word4}?\n Я {word5} каждый {word6} день, как вы и говорили!\n - Вы врёте! Я знаю, что вы этого не делаете,\n иначе вы не были бы таким {word7}!')
                                txt6.destroy()
                                btn.destroy()

                            word6 = txt5.get()
                            label.config(text='Цвет')
                            label.place(x=250, y=100)
                            txt5.destroy()
                            txt6 = Entry(window, width=20, font=("Arial Bold", 20))
                            txt6.place(x=270, y=220)
                            btn.config(command=final)
                            btn.place(x=330, y=300)

                        word5 = txt4.get()
                        label.config(text='Прилагательное')
                        label.place(x=250, y=100)
                        txt4.destroy()
                        txt5 = Entry(window, width=20, font=("Arial Bold", 20))
                        txt5.place(x=270, y=220)
                        btn.config(command=w7)
                        btn.place(x=330, y=300)

                    word4 = txt3.get()
                    label.config(text='Глагол')
                    label.place(x=250, y=100)
                    txt3.destroy()
                    txt4 = Entry(window, width=20, font=("Arial Bold", 20))
                    txt4.place(x=270, y=220)
                    btn.config(command=w6)
                    btn.place(x=330, y=300)

                word3 = txt2.get()
                label.config(text='Вид рыбы')
                label.place(x=250, y=100)
                txt2.destroy()
                txt3 = Entry(window, width=20, font=("Arial Bold", 20))
                txt3.place(x=270, y=220)
                btn.config(command=w5)
                btn.place(x=330, y=300)

            word2 = txt1.get()
            label.config(text='Прилагательное')
            label.place(x=250, y=100)
            txt1.destroy()
            txt2 = Entry(window, width=20, font=("Arial Bold", 20))
            txt2.place(x=270, y=220)
            btn.config(command=w4)
            btn.place(x=330, y=300)

        word1 = txt.get()
        label.config(text='Смешное слово')
        label.place(x=250, y=100)
        txt.destroy()
        txt1 = Entry(window, width=20, font=("Arial Bold", 20))
        txt1.place(x=270, y=220)
        btn.config(command=w3)
        btn.place(x=330, y=300)

    label.config(text='Существительное')
    label.place(x=250, y=100)
    txt = Entry(window, width=20, font=("Arial Bold", 20))
    txt.place(x=270, y=220)
    btn.config(text='Дальше', command=w2)
    btn.place(x=330, y=300)


window = Tk()
word1 = ''
word2 = ''
word3 = ''
word4 = ''
word5 = ''
word6 = ''
word7 = ''
window.geometry('900x450')
window.title("Генератор 'MadLibs'")
label = Label(window,
              text="Привет!\nЭто Генератор 'MadLibs'.\nТвоя задача, по очереди придумать слова,\nопираясь на запрос игры.\nОни будут вставлены в текст,\nи в конце ты его зачитаешь.",
              font=("Arial Bold", 30))
label.place(x=50, y=0)
btn = Button(window, text="Начать", font=("Arial Bold", 30), bg="black", fg="white", command=w1)
btn.place(x=350, y=300)
window.mainloop()
