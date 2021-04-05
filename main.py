from tkinter import *
import os

root = Tk()

root.geometry('480x360')

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

################# 함수 정의 끝 #################

add_kanban = Button(root, padx=10, pady=5, text='열(Column) 추가', command=Add_Column)
add_kanban.pack()

add_card = Button(root, padx=10, pady=5, text='카드(Card) 추가', command=Add_Card)

add_card.pack()

root.mainloop()