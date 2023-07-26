from openpyxl import load_workbook
from docxtpl import DocxTemplate
from json import loads


def compile_contracts():
    with open('json_data', 'r', encoding='utf-8') as file:
        paths = loads(file.readline().rstrip())
        xlpath = paths['xl']
        contractpath = paths['conctract']
        templatepath = paths['template']

    # C:\Users\niks_\Downloads\тест_тестович

    workbook = load_workbook(rf'{xlpath}.xlsx')
    sheet_1 = workbook['Лист1']

    for row in range(2, sheet_1.max_row + 1):
        price = sheet_1.cell(row, 3)
        amount = sheet_1.cell(row, 4)
        total = int(price.value) * int(amount.value)
        total_cell = sheet_1.cell(row, 8)
        total_cell.value = total

    # C:\Users\niks_\Downloads\тестович_тест
    template = DocxTemplate(rf'{templatepath}.docx')
    customers_data = []
    for i in range(2, sheet_1.max_row + 1):
        customers_data.append({
            'name': sheet_1.cell(i, 2).value,
            'company': sheet_1.cell(i, 1).value,
            'start_date': sheet_1.cell(i, 5).value,
            'end_date': sheet_1.cell(i, 6).value,
            'total': sheet_1.cell(i, 8).value
        })


    for customer in customers_data:
        context = {
            'name': customer['name'],
            'company': customer['company'],
            'start_date': customer['start_date'],
            'end_date': customer['end_date'],
            'total': customer['total']
        }
        template.render(context)
        # C:\Users\niks_\Desktop\тестим договоры
        template.save(rf'{contractpath}\{customer["name"]} договор.docx')
