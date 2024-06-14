from datetime import datetime, timedelta
m, n = map( int, input().split() )
year = 2025
date = datetime( year, m, n )
date1 = date + timedelta( -1 )
date2 = date + timedelta( 1 )
date1 = date1.strftime( '%m.%d' )
date2 = date2.strftime( '%m.%d' ) 

print( date1, date2 )

# print( next_date.strftime('%m.%d') )

# m порядковый номер месяца
# n день месяца
