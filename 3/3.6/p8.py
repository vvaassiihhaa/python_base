название = input()
автор = input() 
число_страниц = int( input() )
цена = float( input() )
book = [ название, автор, число_страниц, цена ]
del book[2]
book[ 1 ] = "Пушкин"
book[ 2 ] = book[ 2 ] * 2
print( book )

# название (строка)
# автор (строка)
# число страниц (целое число)
# цена (вещественное число)