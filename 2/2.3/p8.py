# ввод данных
x = int(input())

# вычисляем цену одной ручки со скидкой
discounted_price = x * 0.9

# вычисляем максимальное количество ручек, которые можно купить на 500 рублей
max_pen_count = int(500 // discounted_price)

# вывод результата
print(max_pen_count)