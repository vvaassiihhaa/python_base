n = int( input() )

lst = []

while n > 0:
  if n >= 64:
     n = n - 64
     lst.append( 64 )
     continue

  if n >= 32:
     n = n - 32
     lst.append( 32 )
     continue

  if n >= 16:
     n = n - 16
     lst.append( 16 )
     continue

  if n >= 8:
     n = n - 8
     lst.append( 8 )
     continue

  if n >= 4:
     n = n - 4
     lst.append( 4 )
     continue

  if n >= 2:
     n = n - 2
     lst.append( 2 )
     continue

  if n >= 1:
     n = n - 1
     lst.append( 1 )
     continue

print( *lst )


# 1, 2, 4, 8, 16, 32 и 64