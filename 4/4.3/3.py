b1 = input().lower()
b2 = b1[::-1]
msg = "палиндром" if b1 == b2 else "не палиндром"
print( msg )