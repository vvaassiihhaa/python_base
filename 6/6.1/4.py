import sys
lst_in = list( 
    map( str.strip, sys.stdin.readlines() )
)

d = {}
for i in range( len( lst_in ) ):
    a = lst_in[i].split( "=" )
    n = int( a[0] )
    d[n] = a[1]
    
print(
    *sorted( d.items() )
)    
