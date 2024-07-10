import sys
list_in = sys.stdin.readlines()
list_in = map( str.strip, list_in )
list_in = list( list_in )
d = {}
for num_name in list_in:
  num_name = num_name.split()
  num  = num_name[0]
  name = num_name[1]
  if name in d:
    d[name].append( num )
  else:
    d[name] = [num] 
print( * sorted( d.items() ) )

# print( num_name )
# print( list_in )
# print( * sorted( d.items() ) )