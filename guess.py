max =100
min=1
print(f'Угадываю число от {min} до {max}. Запишите на бумажке')
while True:
    try_int=((max-min)//2)+min
    answer= input (f'{try_int} угадал? "=" если да, > если загаданое число больше, < если загаданое число меньше ')
    if answer == '=':
        print("Кто молодец? я молодец!")
        break
    elif answer == '>':
        min=try_int +1
    elif answer == '<':
        max = try_int -1
    else:
        print('фигня какая-то')

