def is_perfect_square(num):
    if num < 0:
        return False
    sqrt_num = int(num ** 0.5)
    return sqrt_num * sqrt_num == num

while True:
    user_input = input("Введите число: ")
    try:
        number = int(user_input)
        if is_perfect_square(number):
            print("Число является полным квадратом.")
            break
        else:
            print("Число не является полным квадратом. Попробуйте снова.")
    except ValueError:
        print("Ошибка: Введите целое число.")