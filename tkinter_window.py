from tkinter import *
from json import dumps, loads
from compiling import compile_contracts


def save_btn():
    json_data = {
        'xl': xlpath.get(),
        'conctract': contractpath.get(),
        'template': templatepath.get()
    }
    with open("json_data", 'w', encoding='utf-8') as file:
        file.write(dumps(json_data))


def create_window():
    window = Tk()
    window.title('Заполнение договоров данными из excel')
    window.geometry('500x500')

    with open('json_data', 'r', encoding='utf-8') as file:
        paths = loads(file.readline().rstrip())
        xl, contract, template = paths['xl'], paths['conctract'], paths['template']
        if paths and xl and contract and template:
            lbl = Label(window, text='Данные последнего запроса сохранены')
            lbl.grid(column=0, row=5)


    global xlpath
    lbl = Label(window, text='Введите путь до excel-файла')
    lbl.grid(column=0, row=0)
    xlpath = Entry(window, width=10)
    xlpath.grid(column=1, row=0)
    if xl:
        xlpath.insert(0, xl)

    global contractpath
    lbl = Label(window, text='Введите путь по которому будет размещен договор(ы)')
    lbl.grid(column=0, row=1)
    contractpath = Entry(window, width=10)
    contractpath.grid(column=1, row=1)
    if contract:
        contractpath.insert(0, contract)

    global templatepath
    lbl = Label(window, text='Введите путь до шаблона')
    lbl.grid(column=0, row=2)
    templatepath = Entry(window, width=10)
    templatepath.grid(column=1, row=2)
    if template:
        templatepath.insert(0, template)

    btn = Button(window, text='Сохранить введенные данные', command=save_btn)
    btn.grid(column=1, row=3)

    btn = Button(window, text='Составить договоры', command=compile_contracts)
    btn.grid(column=1, row=4)

    window.mainloop()

