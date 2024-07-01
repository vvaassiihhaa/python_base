lst = list( map( int, input().split() ) )

for i in range( len( lst ) ):
  pos = i
  min = lst[ i ]
  for j in range( i + 1, len( lst ) ):
    if lst[ j ] < min:
      min = lst[ j ]
      pos = j
  if i != pos:
    lst[ i ], lst[ pos ] = lst[ pos ], lst[ i ]

print( *lst )


  # print( lst[ i ] )