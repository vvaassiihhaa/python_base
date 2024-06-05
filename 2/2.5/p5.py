import math
f = float( input() )
f_int = math.floor( f )
res = bool( f_int % 3 == 0 )
print( res )