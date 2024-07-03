cities = input().split()
a = [ _ for _ in cities if len( _ ) > 5 ]
print( *a )