ll = list( map( int, input().split() ) )
l2 = []
for dd in ll:
  l2 += list( dd ) * 2
print( *l2 )