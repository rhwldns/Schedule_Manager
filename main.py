from tkinter import *
import os
import glob

root = Tk()

root.geometry('480x360')
root.title("Schedule Manager")

# Label, Entry 등 먼저 정의하고 나중에 한꺼번에 .pack() 하기
# 용어 정의
## 카드 : Github의 column

################# 함수 정의 #################

def Add_Column():
    aw = Toplevel(root)
    Infor_Txt = Label(aw, text='열(Column) 이름을 입력하세요.')
    input_name = Entry(aw)
    aw.geometry('480x360')

    Infor_Txt.pack()
    input_name.pack()


    def Add_Column2():
        kanban_name = input_name.get()
        if os.path.isdir('Columns/'):
            with open(f'Columns/{kanban_name}.txt', 'a') as f:
                f.write('1')
                f.seek(0)
                f.truncate()

        else:
            os.mkdir('Columns/')

            with open(f'Columns/{kanban_name}.txt', 'a', encoding='UTF-8') as f:
                f.write('1')
                f.seek(0)
                f.truncate()
        donetxt = Label(aw, text='열(Column) 생성이 완료되었습니다.')
        donetxt.pack()

    done_b = Button(aw, padx=10, pady=5, text='완료', command=Add_Column2)
    done_b.pack()


def Add_Card():
    a = Toplevel(root)
    a.geometry('480x150')
    Infor_txt2 = Label(a, text='카드를 추가할 열(Column)의 이름을 작성해주세요.')
    Infor_txt2.pack()

    cardcontent = Entry(a)
    cardcontent.pack()

    def addcard():
        ct = cardcontent.get()

        if os.path.isfile(f"Columns/{ct}.txt"):
            aa = Toplevel(a)
            aa.geometry('480x360')
            infortxt = Label(aa, text='카드 정보(내용)를 입력하세요.')
            infortxt.pack()

            cardinfo = Entry(aa)
            cardinfo.pack()

            def ADDCARD():
                c = cardinfo.get()

                with open(f'Columns/{ct}.txt', 'a', encoding="UTF-8") as f:
                    f.write(str(c) + '\n')

                donet = Label(aa, text='카드 정보(내용) 추가를 완료했습니다.')
                donet.pack()

            db = Button(aa, padx=10, pady=5, text='완료', command=ADDCARD)
            db.pack()


    doneb = Button(a, padx=10, pady=5, text = '완료', command=addcard)
    doneb.pack()

def config():
    a = Toplevel(root)
    a.geometry('480x360')
    CheckVar1 = IntVar()

    CheckVar2 = IntVar()

    c1 = Checkbutton(a, text="다크 모드", var=CheckVar1)

    c2 = Checkbutton(a, text="화이트 모드", var=CheckVar2)

    c1.pack()
    c2.pack()

    def change_bgcolor():
        if CheckVar1.get() == 1:

            root['bg'] = '#000000'

        elif CheckVar2.get() == 1:

            root['bg'] = '#ffffff'

        else:
            pass


    donb = Button(a, padx=10, pady=5, text='완료', command=change_bgcolor)
    donb.pack()


def see_cc():
    a = Toplevel(root)
    file_list = os.listdir("Columns/")
    b = ''

    for file in file_list:
        f = file.replace(".txt", " ")
        b += str(file + '\n')
    l = Label(a, text=f'열(Column) 목록입니다.\n조회하고 싶은 열의 이름을 작성해주세요.\n\n{b}')
    l.pack()
    e = Entry(a)
    e.pack()

    def seeCC():
        cn = e.get()
        aa = Toplevel(root)


        if os.path.isfile(f'./Columns/{cn}.txt'):
            print(1)
            with open(f"./Columns/{cn}.txt", 'r', encoding='UTF-8') as ff:
                rl = ff.readlines()

            for i in rl:
                al = Label(aa, text=f"{i}")
                al.pack()

    doneb = Button(a, padx=10, pady=5, text='완료', command=seeCC)
    doneb.pack()

################# 함수 정의 끝 #################

add_kanban = Button(root, height=2, width=15, text='열(Column) 추가', command=Add_Column)
add_card = Button(root, height=2, width=15, text='카드 (Card) 추가', command=Add_Card)
see_cc = Button(root, height=2, width=15, text='열 & 카드 보기', command=see_cc)
setting_b = Button(root, height=2, width=15, text='설정', command=config)

add_card.pack()
add_kanban.pack()

add_kanban.place(x=30, y=50)
add_card.place(x=30, y=100)
see_cc.place(x=30, y=150)
setting_b.place(x=30, y=200)

root.mainloop()