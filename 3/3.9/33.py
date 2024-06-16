matrix = [
    list( map( int, input().split() ) ),
    list( map( int, input().split() ) ),
    list( map( int, input().split() ) )
]

res = []
res.append( matrix [0][-1] )
res.append( matrix [1][-1] )
res.append( matrix [2][-1] )

print( *res )