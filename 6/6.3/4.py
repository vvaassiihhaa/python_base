cities = input().split()

t = tuple( cities )
if "Москва" not in t :
  t += ( "Москва", )
print( *t ) 

# print( cities )