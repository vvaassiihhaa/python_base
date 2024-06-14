m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
menu = int( input() )
start = m.find( f"{menu}" )
end = m.find( '\n', start ) 

if end == -1:
    res = m[ start : ]
else:
  res = m[ start : end ]

print( res )