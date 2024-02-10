from logger import input_data, print_data, edit_record, delete_record

def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что вы хотели сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Изменить строку \n'
          '4 - Удалить строку \n')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 4:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        print_data()
        filename = input('Из какого файла изменить? 1 или 2: ')
        if filename == '1':
            filename = 'data_first_variant.csv'
        elif filename == '2':
            filename = 'data_second_variant.csv'
        else:
            print('Ошибка! Неверный ввод файла.')
            return

        record_number = int(input('Какую строку изменить? (Введите номер строки): '))
        edit_record(filename, record_number)
    elif command == 4:
        print_data()
        filename = input('Из какого файла удалить строку? 1 или 2: ')
        if filename == '1':
            filename = 'data_first_variant.csv'
        elif filename == '2':
            filename = 'data_second_variant.csv'
        else:
            print('Ошибка! Неверный ввод файла.')
            return

        record_number = int(input('Какую строку удалить? (Введите номер строки): '))
        delete_record(filename, record_number)

if __name__ == "__main__":
    interface()
