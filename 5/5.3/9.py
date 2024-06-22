cities = input().split()
last = ""
res = "НЕТ"
for city in cities:
    if last == city[0].lower():
        res = "ДА"
        break
    last = city[-1]
    if last in 'ьъы':
        last = city[-2]
print( res )
#    print( city[-1] )
#    print( city )

# ьъы
# Москва Астрахань Новгород Димитровград Душанбе