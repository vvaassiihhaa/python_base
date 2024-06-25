fd = list( map( float, input().split() ) )
min = fd[0]
for d in fd:
  if d < min:
    min = d
print( min )