import math

# ввод данных
n, m = map(int, input().split())

# общее количество людей
total_people = n + m

# минимальное количество автобусов, необходимых для перевозки
buses_needed = math.ceil(total_people / 20)

# вывод результата
print(buses_needed)
