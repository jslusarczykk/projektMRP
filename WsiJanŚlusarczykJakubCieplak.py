from openpyxl import Workbook
#ZAINSTALLOWAĆ pip install openpyxl

#Członkowie grupy: Jan Ślusarczyk, Jakub Cieplak

g = int(input("Podaj liczbę garniturów do produkcji: "))
x = int(input("Podaj liczbę garniturów na stanie: "))
gz = int(input("Podaj liczbę guzików na stanie: "))
k = int(input("Podaj liczbę korpusów na stanie: "))
r = int(input("Podaj liczbę rękawów na stanie: "))
w = int(input("Podaj liczbę wełny na stanie: "))
n = int(input("Podaj liczbę nici na stanie: "))
w1 = int(input("Podaj liczbę waterunków na stanie: "))
pc = int(input("Podaj cenę jednego garnituru: "))
pw = int(input("Podaj cenę 1m wełny: "))
pn = int(input("Podaj cenę 1m nici: "))
t = 8  # t - całkowity czas produkcji wszystkiego

#Zakładamy, że zamówienie nie może być mniejsze niż x rzecz na stanie 
#Nasze dane zakładają że mniejsze zamówienie = dłuższa dostawa
if g > 10:  # dostawa # zakładamy ze nasz warsztat w ciagu 8 tygodni wyprodukuje 10 garniturów
    t += int(g / 10)

if w < g / 2:  # safety stock # jesli mamy malo welny na stanie to wydłuzamy czas o tydzien
    t += 1
p = g * pc  # cena

if w >= 10:  # znizka przy zakupie 10 metrow lub wiecej wełny
    p -= pw / 10  # przy zakupie 10 wełn

if n >= 3000:  # znizka przy zakupie 3000 metrow lub wiecej nici
    p -= pn * 0.3

if w1 < 5:
    p += p / 30  # przy zakupie mniej niż 5 waterunków podwyżka ceny


def create_garments_table(ws):
    ws.append(["poziom 0 - garnitury", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", "", "", "", "", "", "", "", g])
    ws.append(["wstępny zapas", x, x, x, x, x, x, x, ""])
    ws.append(["potrzeby netto", "", "", "", "", "", "", "", g-x])
    ws.append(["zaplanowany odbiór", "", "", "", "", "", "", "", g])


def create_buttons_table(ws):
    ws.append(["poziom 1 - guziki", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", "", "", "", g*6, "", g*10, "", ""])
    ws.append(["wstępny zapas", gz, gz, gz, gz, "", "", "", ""])
    ws.append(["potrzeby netto", "", "", "", g*4-gz, "", g*10, "", ""])
    ws.append(["zamówienie",g*4, "", "", g*10, "", "", "", ""])
    ws.append(["zaplanowany odbiór", "", "", "", g*4, "", g*10, "", ""])


def create_body_table_korpus(ws):
    ws.append(["poziom 2 - korpus", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", "", "", g/2, "", g, "", "", ""])
    ws.append(["wstępny zapas", k, k, k, "", "", "", "", ""])
    ws.append(["potrzeby netto", "", "", g/2-k, "", g, "", "", ""])
    ws.append(["zaplanowany odbiór", "", "", g/2, "", g, "", "", ""])


def create_body_table_rekaw(ws):
    ws.append(["poziom 2 - rękaw", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", "", "", g, "", g*2, "", "", ""])
    ws.append(["wstępny zapas", r, r, r, "", "", "", "", ""])
    ws.append(["potrzeby netto", "", "", g-r, "", g*2, "", "", ""])
    ws.append(["zaplanowany odbiór", "", "", g, "", g*2, "", "", ""])


def create_body_table_welna(ws):
    ws.append(["poziom 3 - wełna", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", g*2, "", "", "", "", "", "", ""])
    ws.append(["wstępny zapas", w, "", "", "", "", "", "", ""])
    ws.append(["potrzeby netto", 2*g-w, "", "", "", "", "", "", ""])
    ws.append(["zaplanowany odbiór", 2*g, "", "", "", "", "", "", ""])


def create_body_table_waterunek(ws):
    ws.append(["poziom 3 - waterunek", "", "", "", "", "", "", "", ""])
    ws.append(["", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", g * 2, "", "", "", "", "", "", ""])
    ws.append(["wstępny zapas", w1, "", "", "", "", "", "", ""])
    ws.append(["potrzeby netto", g * 2 - w1, "", "", "", "", "", "", ""])
    ws.append(["zaplanowany odbiór", g * 2 , "", "", "", "", "", "", ""])


def create_body_table_nic(ws):
    ws.append(["poziom 3 - nić", "", "", "", "", "", "", "", ""])
    ws.append(["", "", "", "", "", "", "", "", ""])
    ws.append(["tydzień", 1, 2, 3, 4, 5, 6, 7, 8])
    ws.append(["potrzeby brutto", "", g * 500, "", "", "", "", "", ""])
    ws.append(["wstępny zapas", n, n, "", "", "", "", "", ""])
    ws.append(["potrzeby netto", "", g * 500 - n, "", "", "", "", "", ""])
    ws.append(["zamówienie",g*500, "", "", "", "", "", "", ""])
    ws.append(["zaplanowany odbiór", "", g * 500, "", "", "", "", "", ""])


wb = Workbook()
ws = wb.active
ws.title = "Tabela"

ws.append(["Łączna cena zamówienia: ",p,"Zł","Łączny czas z dostawą: ",t,"tygodni"])
ws.append(["", "", "", "", "", "", "", "", ""])

create_garments_table(ws)
ws.append(["", "", "", "", "", "", "", "", ""])
ws.append(["", "", "", "", "", "", "", "", ""])
create_buttons_table(ws)
ws.append(["", "", "", "", "", "", "", "", ""])
ws.append(["", "", "", "", "", "", "", "", ""])
create_body_table_korpus(ws)
ws.append(["", "", "", "", "", "", "", "", ""])
ws.append(["", "", "", "", "", "", "", "", ""])
create_body_table_rekaw(ws)
ws.append(["", "", "", "", "", "", "", "", ""])
ws.append(["", "", "", "", "", "", "", "", ""])
create_body_table_welna(ws)
ws.append(["", "", "", "", "", "", "", "", ""])
ws.append(["", "", "", "", "", "", "", "", ""])
create_body_table_waterunek(ws)
ws.append(["", "", "", "", "", "", "", "", ""])
ws.append(["", "", "", "", "", "", "", "", ""])
create_body_table_nic(ws)

wb.save("WsiJanŚlusarczykJakubCieplak.xlsx")
print("Arkusz excel został pomyślnie wygenerowany")
