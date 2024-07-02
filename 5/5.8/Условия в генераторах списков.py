a = [x for x in range(-5, 5) if x < 0]
print( a )

a = [x for x in range(-5, 5) if x % 2 != 0]
print( a )

a = [x for x in range(-6, 7) if x % 2 == 0 and x % 3 == 0]
print( a )

cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
a = [city for city in cities if len(city) < 7]
print( a )

print()

d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
print( d )
a = ["четное" if x % 2 == 0 else "нечетное" for x in d]
print( a )

a = [x + 2 for x in d]
print( a )

print()

a = ["четное" if x % 2 == 0 else "нечетное"
     for x in d
     if x > 0
]
print( a )
