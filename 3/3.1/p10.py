hello, python = map( str, input().split() )
res = str( hello in python )
a = hello == python
res = res + " " + str( a )
a = hello > python
res = res + " " + str( a )
a = hello < python
res = res + " " + str( a )
print( res )