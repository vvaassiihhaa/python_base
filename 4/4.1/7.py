cities = input().split()

if "Москва" in cities:
    # ind = cities( "Москва" )
    cities .remove( "Москва" )
    
print( *cities )