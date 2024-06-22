cities = input().split()
last = cities[0][0].lower()
res = "ДА"
for city in cities:
    if last == city[0].lower() and res == "ДА":
        res = "ДА"
    else:
        res = "НЕТ"
    last = city[-1]
    if last in 'ьъы':
        last = city[-2]
print( res )
#    print( city[-1] )
#    print( city )

# test #2
# input: Вологда Архангельск Курск Москва
# output: НЕТ

# ьъы
# Москва Астрахань Новгород Димитровград Душанбе