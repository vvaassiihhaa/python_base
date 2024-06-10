subscribers = list( map( int, input().split() ) )
lst = sorted( subscribers, reverse = True )
print( *lst )