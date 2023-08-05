import random

flag=True
while flag:
    num=int(random.randint(1, 100))
    print('Добро пожаловать в числовую угадайку :)')
    num_user=input('Мы загадали число, а вы угадайте какое. Введите число: от 1 до 100:')

    #Проверка на число и диапазон
    def is_valid(num_user):
        while True:
            num_user=num_user
            if not num_user.isdigit():
                num_user=input('Вы ввели не число. Введите число: от 1 до 100:')
            elif not 0<int(num_user)<101:
                num_user=input('Введите число из диапазона от 0 до 100:')
            else:
                return int(num_user)
        return int(num_user)    
    
    num_user=is_valid(num_user)
    
    #Сравнение введенного числа с загаданным
    def check_num_user(num, num_user):
        if num_user<num:
            num_user=is_valid(input('Ваше число МЕНЬШЕ. Попробуйте еще раз...'))
            check_num_user(num, num_user)
        elif num_user>num:
            num_user=is_valid(input('Ваше число БОЛЬШЕ. Попробуйте еще раз...'))
            check_num_user(num, num_user)
        else:
            print('Вы угадали, поздравляем!')
            
    check_num_user(num, num_user)
    
    print('Hakyna-Matata!')
    flag = True if input('Хотите сыграть еще раз? Нажмите + и enter ') == '+' else False