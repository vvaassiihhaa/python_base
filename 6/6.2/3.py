s = input().upper()
d = {}
d["А"] = ".-"
d["Б"] = "-..."
d["В"] = ".--"
d["Г"] = "--."
d["Д"] = "-.."
d["Е"] = "."
d["Ё"] = "."
d["Ж"] = "...-"
d["З"] = "--.."
d["И"] = ".."
d["Й"] = ".---"
d["К"] = "-.-"
d["Л"] = ".-.."
d["М"] = "--"
d["Н"] = "-."
d["О"] = "---"
d["П"] = ".--."
d["Р"] = ".-."
d["С"] = "..."
d["Т"] = "-"
d["У"] = "..-"
d["Ф"] = "..-."
d["Х"] = "...."
d["Ц"] = "-.-."
d["Ч"] = "---."
d["Ш"] = "----"
d["Щ"] = "--.-"
d["Ъ"] = "--.--"
d["Ы"] = "-.--"
d["Ь"] = "-..-"
d["Э"] = "..-.."
d["Ю"] = "..--"
d["Я"] = ".-.-"
d[" "] = "-...-"

l = len( s )
for i in range( l - 1 ) :
    si = s[ i ]
    print( d[ si ], end = " " )

last_letter = s[ l - 1 ]
print( d[ last_letter ] )

#
#for i in range( l ) :
#  print( s[i] )
  # print( d[ s[i] ], end = " " )
#print( d[ l ] )

#
#
# А    .-	М    --		Ш    ----
# Б    -...	Н    -.		Щ    --.-
# В    .--	О    ---	Ъ    --.--
# Г    --.	П    .--.	Ы    -.--
# Д    -..	Р    .-.	Ь    -..-
# Е (Ё)    .	С    ...	Э    ..-..
# Ж    ...-	Т    -		Ю    ..--
# З    --..	У    ..-	Я    .-.-
# И    ..	Ф    ..-.	' '    -...-
# Й    .---	Х    ....	 
# К    -.-	Ц    -.-.	 
# Л    .-..	Ч    ---.	 