def get_number_of_records(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for line in file) // 4  

def input_user_data():
    name = input("Введите имя: ")
    surname = input("Введите фамилия: ")
    phone = input("Введите телефон: ")
    address = input("Введите адрес: ")
    return name, surname, phone, address

def input_data():
    name, surname, phone, address = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{address}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{address}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            record_number = get_number_of_records('data_first_variant.csv') + 1
            offset = (record_number - 1) * 4
            file.write(f'Запись {record_number}\n'
                       f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{address}\n\n')

    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            record_number = get_number_of_records('data_second_variant.csv') + 1
            offset = (record_number - 1) * 4
            file.write(f'Запись {record_number};{name};{surname};{phone};{address}\n\n')

def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
