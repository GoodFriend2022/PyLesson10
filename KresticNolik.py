import random


def show_field(array):
    for i in range(3):
        index = i * 3
        print(array[index], array[index + 1], array[index + 2])
    print('')

def check_win(array):
    for i in range(3):
        index = i * 3
        if array[index] == array[index + 1] == array[index + 2]:
            print(f'Победили >>{array[index]}<<')
            return True
        elif array[i] == array[i + 3] == array[i + 6]:
            print(f'Победили >>{array[index]}<<')
            return True
    if array[0] == array[4] == array[8]:
        print(f'Победили >>{array[index]}<<')
        return True
    elif array[2] == array[4] == array[6]:
        print(f'Победили >>{array[index]}<<')
        return True
    return False

def create_array():   
    array = []
    for i in range(1, 10):
        array.append(i)
    return array
    
def user(array):
    number_user = int(input('Введите номер ячейки, куда хотите поставить крестик: '))
    while array[number_user - 1] == 'X' or array[number_user - 1] == 'O':
        number_user = int(input('Этотноме занят попробуйте еще раз: '))
    array[number_user - 1] = 'X'
    show_field(array)
    return array

def cpu(array):
    number_cpu = random.randint(1, 9)
    while array[number_cpu - 1] == 'X' or array[number_cpu - 1] == 'O':
        number_cpu = random.randint(1, 9)
    array[number_cpu - 1] = 'O'
    show_field(array)
    return array

def game(array):
    for i in range(10):
        if check_win(array):
            return print('Спасибо за игру!!!')
        else:
            user(array)
            cpu(array)

field = create_array()
show_field(field)
game(field)

    
    


            