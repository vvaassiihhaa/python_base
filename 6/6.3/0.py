lst = [1]
t   = (1,)
# print( f"Размер списка {lst.__sizeof__()}" )
# print( f"Размер кортежа {t.__sizeof__()}" )
a = ()
b = tuple()
# print( type( a ), type( b ) )
a = ( "abc", 2, [1,2], True, 2, 5 )

count_abc = a.count( "abc" )
count_2   = a.count( 2 )
count_a   = a.count( "a" )

print( f"{a} \ncount_abc {count_abc} count_2 {count_2} count_a {count_a}" )