from json import dumps
# программа падает если в ней лежат невалидные данные. этот костыль помогает
# C:\Users\niks_\Downloads\тест_тестович
# C:\Users\niks_\Desktop\тестим договоры
# шаблон
# C:\Users\niks_\Downloads\тестович_тест

json_data = {
        'xl': r'C:\Users\niks_\Downloads\client_data',
        'conctract': r'C:\Users\niks_\Desktop\for_contracts',
        'template': r'C:\Users\niks_\Downloads\template'
    }
with open("json_data", 'w', encoding='utf-8') as file:
    file.write(dumps(json_data))
