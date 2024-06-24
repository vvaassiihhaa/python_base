st = input().replace( " ", "" ) + "+"
num = ""
S = 0
oper = 1
for ii in st:
  if ii.isdigit():
    num += ii
  else:
    S += int( num ) * oper  
    num = ""
    if ii == "+":
      oper = 1
    else:
      oper = -1
        
print( str( S ) )

# 0 - 1 + 2 - 3 + 4 - 5 + 6