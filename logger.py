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

def edit_record(filename, record_number):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if 1 <= record_number <= len(lines) / 4:
        start_index = (record_number - 1) * 4
        end_index = start_index + 4

        record = lines[start_index:end_index]
        print('Старая запись:')
        print(''.join(record))

        name = input("Введите новое имя: ")
        surname = input("Введите новую фамилию: ")
        phone = input("Введите новый телефон: ")
        address = input("Введите новый адрес: ")

        new_record = [f'Запись {record_number}\n', f'{name}\n', f'{surname}\n', f'{phone}\n', f'{address}\n\n']

        lines[start_index:end_index] = new_record

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(''.join(lines))
        print('Запись успешно изменена.')
    else:
        print('Ошибка! Некорректный номер записи.')

def delete_record(filename, record_number):
    lines_to_keep = []
    current_record_lines = []
    current_record_number = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip().startswith('Запись'):
                current_record_number += 1
                if current_record_lines:
                    lines_to_keep.extend(current_record_lines)
                    current_record_lines = []

            if current_record_number == record_number:
                continue

            current_record_lines.append(line)

        if current_record_lines:
            lines_to_keep.extend(current_record_lines)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines_to_keep)

    print('Запись успешно удалена.')
