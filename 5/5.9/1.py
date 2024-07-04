import sys

s = sys.stdin.readlines()
lst_in = [
    list( map( int, x.strip().split() ) ) 
    for x in s
]

a = [ 
    lst_in[i][j]
    for i in range( len( lst_in ) )[::-1] 
    for j in range( len( lst_in[0] )  )[::-1]   
]

print( *a )