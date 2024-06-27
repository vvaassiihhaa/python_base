import sys
lst_in = list( map( str.strip, sys.stdin.readlines() ) )
for url in lst_in:
  while url.count( "  " ):
    url = url.replace( "  ", " " )
  url = url.replace( " ", "-" )
  print( url )


# django chto  eto takoe    poryadok ustanovki
# url = "django chto  eto takoe    poryadok ustanovki"
# if True:

