numbers = [num for num in range(100, 1000) if num % 17 == 0]

print(' '.join(map(str, numbers)))
print(f'Количество трехзначных натуральных чисел, делящихся на 17: {len(numbers)}')