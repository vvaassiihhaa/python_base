lst = input().split()
cities = [ "Москва", "Тверь", "Вологда" ]
lst = cities + lst  
print( *lst )