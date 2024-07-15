import sys
lst_in = sys.stdin.readlines()
lst_in = map( str.strip, lst_in )
lst_in = list( lst_in )
d = {}
# print( *lst_in )
for lst in lst_in:
  lst = lst.split()    
  # print( lst )
  bd = lst[0]
  if bd in d:
    d[ bd ] = d[ bd ] + ", " + lst[1]
  else:
    d[ bd ] = lst[1]
# print( d )
for key, value in d.items():
  print( f"{key}: {value}")
      