try:
    age = int(input("Введите ваш возраст: "))

    if age >= 18:
        print('Доступ разрешен')
    else:
        print('Доступ запрещен')
except ValueError:
    print("Ошибка: введите корректное число.")
