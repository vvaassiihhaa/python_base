lst = input().split()
d = {}
for number in lst:
  if number not in d:
    d[ number ] = number
print( *d )