k = int( input() )
k = k % 7 - 1
week = [ 
    'понедельник',  
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
    'воскресенье'
]
print( week[k] )

# 1 <= k <= 365
# 1 понедельник
# 2 вторник
# 3 среда
# 4 четверг
# 5 пятница 
# 6 суббота 
# 7 воскресенье