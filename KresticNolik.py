import random
import os

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
        print(f'Победили >>{array[0]}<<')
        return True
    elif array[2] == array[4] == array[6]:
        print(f'Победили >>{array[2]}<<')
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
        number_user = int(input('Этот номер занят попробуйте еще раз: '))
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
    who_player = player()
    for i in range(10):
        if check_win(array):
            return print('Спасибо за игру!!!')
        if who_player == 'user':
            user(array)
            who_player = 'cpu'
        elif who_player == 'cpu':
            cpu(array)
            who_player = 'user'
    return print('Что-то пошло не так. Перезапустите игру и попробуйте еще раз')

def player():
    players = '1 - user \n2 - cpu \n'
    print(players)
    number = int(input('Выберите кто будет ходить первым >> '))
    if number == 1:
        return 'user'
    elif number == 2:
        return 'cpu'
    return print('Такой номер в меню отсутствует')

os.system('cls')
field = create_array()
show_field(field)
game(field)

    
    


            