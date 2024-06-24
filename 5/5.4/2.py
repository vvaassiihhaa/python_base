st = input()
res = st[:3]

for ii in range( 3, len( st ) ):
  if st[ii] in '0123456789':
    res += "x"
  else:  
    res += st[ii]

if res == "+7(xxx)xxx-xx-xx":
    print( "ДА" )
else:
    print( "НЕТ" )


# print( res )

# +7(123)456-78-99


# for ii in st:
#   res += ii
