abcdef = int( input() )
a = abcdef // 100000
abcdef = abcdef % 100000  
b = abcdef // 10000
abcdef = abcdef % 10000 
c = abcdef // 1000
abcdef = abcdef % 1000
d = abcdef // 100
abcdef = abcdef % 100
e = abcdef // 10
f = abcdef % 10
res = a + b + c == d + e + f
if res:
    print( "ДА" )
else:
    print( "НЕТ" )
# print( a, b, c, d, e, f )
