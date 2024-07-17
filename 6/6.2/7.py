things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

N = int( input() ) * 1000
ssoboy = []

ves = 0
while ves <= N:
  max = 0
  for key, value in things.items():
    if value > max and ( ves + value ) <= N:
      max = value
      max_thing = key
  ves += things.pop( max_thing, 0 )
  print( ves )

  if max == 0:
    ves = N + 1

  if ves <= N:
    ssoboy.append( max_thing )
    print( max_thing )

print( *ssoboy )     

# print( N )

# 5240
# палатка
# 7370
# брезент
# 8570
# удочка
# 9570
# брюки
# 10390