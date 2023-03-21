def print_num():
    for i in data:
        print('\t'.join(i))


def search_():
    print('искать по фамилии или по имени?[0-Имя; 1-фамилия]')
    k = int(input())
    print(f'Введите {"имя" if k == 0 else "фамилию"}')
    search_query = input()
    for i in data:
        if search_query in i[0].split()[k]:
            print('\t'.join(i))


def change():
    phone = input('Введите номер телефона: ')
    flag = True
    for i in range(len(data)):
        if data[i][1] == phone:
            data[i][0] = f'{input("Введите имя: ")} {input("Введите фамилию: ")}'
            flag = False
            break
    if flag:
        print('Номер телефона не найден')

with open('data.txt', 'r', encoding='Windows-1251') as file:
    data = list(map(lambda x: x.rstrip().split(';'), file.readlines()))
while True:
    print('Что вы хотите сделать?')
    print('1. Изменить')
    print('2. Вывести')
    print('3. Поиск')
    print('4. Exit')
    a = input()
    if a == '1':
        change()
    elif a == '2':
        print_num()
    elif a == '3':
        search_()
    elif a == '4':
        break
with open('data.txt', 'w') as file:
    file.write('\n'.join(map(lambda x: ";".join(x), data)))
    
