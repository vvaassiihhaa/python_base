a = [ 1, 2 ]
# a = a.append( 100 )
a.append( 3 )
# a.append( (3,2,1) )
print( a )
c = a.copy()
# c = list(a)
print( id(c) )
print( id(a) )