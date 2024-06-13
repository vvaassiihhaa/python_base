a, b, c, d = map( int, input().split() )

res1 = a - c - 2 
res2 = b - d - 2 
res3 = a - d - 2 
res4 = b - c - 2 

if ( res1 >= 0 and res2 >= 0 ) or ( res3 >= 0 and res4 >= 0 ):
    print( "ДА" )
else:
    print( "НЕТ" )


# 12 5 7 2
# c + 1
# d + 1
