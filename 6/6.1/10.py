import sys
list_in = sys.stdin.readlines()
list_in = map( str.strip, list_in )
list_in = list( list_in )
d = {}
for adres in list_in:
  if adres in d:
    print( f"Взято из кэша: {d[adres]}" )
  else:
    str = "HTML-страница для адреса " + adres
    d[adres] = str
    print( str )

# print( adres )
# print( list_in )