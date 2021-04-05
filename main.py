from tkinter import *
import os

root = Tk()

root.geometry('480x360')

# Label, Entry 등 먼저 정의하고 나중에 한꺼번에 .pack() 하기
# 용어 정의
## 카드 : Github의 column

# 함수 정의
def Add_card():
    aw = Toplevel(root)
    Infor_Txt = Label(aw, text='카드 이름을 입력하세요.')
    input_name = Entry(aw)
    aw.geometry('480x360')

    Infor_Txt.pack()
    input_name.pack()


    def Add_card2():
        kanban_name = input_name.get()
        if os.path.isdir('Cards/'):
            with open(f'Cards/{kanban_name}.txt', 'a') as f:
                f.write('1')
                f.seek(0)
                f.truncate()

        else:
            os.mkdir('Cards/')

            with open(f'Cards/{kanban_name}.txt', 'a', encoding='UTF-8') as f:
                f.write('1')
                f.seek(0)
                f.truncate()
        donetxt = Label(aw, text='카드 생성이 완료되었습니다.')
        donetxt.pack()

    done_b = Button(aw, padx=10, pady=5, text='완료', command=Add_card2)
    done_b.pack()


add_kanban = Button(root, padx=10, pady=5, text='카드 추가', command=Add_card)
add_kanban.pack()

root.mainloop()