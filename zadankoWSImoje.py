#stała g - liczba garniturów 
# g-x = liczba garniturów netto
#g = int(input("Podaj liczbę garniturów do produkcji: "))
#x = int(input("Podaj liczbę garniturów na stanie: "))
#gz = int(input("Podaj liczbę guzików na stanie: "))
#k = int(input("Podaj liczbę korpusów na stanie: "))
#r = int(input("Podaj liczbę rękawów na stanie: "))
#w = int(input("Podaj liczbę wełny na stanie: "))
#n = int(input("Podaj liczbę nici na stanie: "))
#w1 = int(input("Podaj liczbę waterunków na stanie: "))
#pc = int(input("Podaj cenę jednego garnituru: "))
#pw = int(input("Podaj cenę 1m wełny: "))
#pn = int(input("Podaj cenę 1m nici: "))
#t = 8 # t - całkowity czas produkcji wszystkiego

#if g>10:				#dostawa	#zakładamy ze nasz warsztat w ciagu 8 tygodni wyprodukuje 10 garniturów	
#	t+=int(g/10)
			
#if w < g/2 : 			#safety stock	#jesli mamy malo welny na stanie to wydłuzamy czas o tydzien
#	t+=1				
#p=g*pc # cena

#if w >=10: #znizka przy zakupie 10 metrow lub wiecej wełny
#    p-=pw/10 #przy zakupie 10 wełn 
#if n>=3000: #znizka przy zakupie 3000 metrow lub wiecej nici
#    p-=pn*0.3 
#if w1 < 5 : 
#    p+=p/30 #przy zakupie mniej niż 5 waterunków podwyżka ceny
    
#przykładowa tabelka dla poziomu zero
#print("|      Poziom 0      |   garnitury                                             |")
#print("|      Tydzień       |       1       |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
#print(f"|  Potrzeby brutto   |                                                     {g}  |")
#print(f"|   Wstępny zapas    |      {x}       {x}       {x}       {x}   {x}   {x}   {x}   {x}      |")

		
# Dane do tabelki
g = 1000  # Przykładowa wartość potrzeb brutto
x = 2    # Przykładowy znak dla wstępnego zapasu

# Wyświetlanie tabelki
# Dane do tabelki
g = 1000  # Przykładowa wartość potrzeb brutto
x = "X"   # Przykładowy znak dla wstępnego zapasu

# Wyświetlanie tabelki
print("|      Poziom 0      |   garnitury                                             |")
print("|      Tydzień       |       1       |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
print(f"|  Potrzeby brutto   |                                                     {g}  |")

# Formatowanie wstępnego zapasu
initial_stock = f"|   Wstępny zapas    |"
for week in range(1, 8):
    if week == 1:
        initial_stock += f"      {x}       "  # Dla tygodnia 1 użyj jednego odstępu
    else:
        initial_stock += f"   {x}   "  # Dla pozostałych tygodni użyj większego odstępu

initial_stock += "|"
print(initial_stock)
