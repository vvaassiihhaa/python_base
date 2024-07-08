s = input().split()
d = {}
for number in s:
  plus_number = number[:2]
  if plus_number in d:    
    d[plus_number].append( number ) # append
  else:
    d[plus_number] = [number]    

print( *sorted( d.items() ) )

# Sample Input:

# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890

# print( s )

  # print( plus_number )
