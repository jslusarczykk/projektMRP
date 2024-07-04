def calculate_garment_requirements(garments_needed, garments_in_stock):
    # Obliczenia dotyczące garniturów (poziom 0)
    net_garments = garments_needed - garments_in_stock
    if net_garments > 0:
        # Obliczenie czasu dostawy
        if garments_needed <= 10:
            lead_time = 8
        else:
            lead_time = 8 + int(garments_needed / 10)

        # Obliczenie ogólnego kosztu garniturów
        pc = float(input("Podaj cenę jednego garnituru: "))
        total_cost = pc * garments_needed

        return net_garments, total_cost, lead_time
    else:
        return 0, 0, 0  # Brak zapotrzebowania na nowe garnitury


def generate_level_zero_table():
    # Poziom 0 - Garnitury
    print("\nPoziom 0 - Garnitury")
    g = int(input("Podaj liczbę garniturów do zrobienia: "))
    x = int(input("Podaj liczbę garniturów w zapasie: "))

    net_garments, total_cost, lead_time = calculate_garment_requirements(g, x)

    # Generowanie tabelki
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 9):
        if week == 1:
            gross_requirements = g
            initial_inventory = x
            net_requirements = net_garments
            planned_receipt = g
        else:
            gross_requirements = 0
            initial_inventory = 0
            net_requirements = 0
            planned_receipt = 0

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")


def generate_level_one_table():
    # Poziom 1 - Guziki
    print("\nPoziom 1 - Guziki")
    g = int(input("Podaj liczbę garniturów do zrobienia: "))

    # Obliczenia dotyczące guzików (poziom 1)
    gz = g * 10
    gz_week_4 = g * 4
    gz_week_6 = g * 10

    # Generowanie tabelki
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 7):
        if week == 4:
            gross_requirements = gz_week_4
            initial_inventory = gz
            net_requirements = gz_week_4 - gz
            planned_receipt = gz_week_4
        elif week == 6:
            gross_requirements = gz_week_6
            initial_inventory = gz_week_4
            net_requirements = gz_week_6 - gz_week_4
            planned_receipt = gz_week_6
        else:
            gross_requirements = 0
            initial_inventory = 0
            net_requirements = 0
            planned_receipt = 0

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")


def generate_level_two_table():
    # Poziom 2 - Korpusy i Rękawy
    print("\nPoziom 2 - Korpusy i Rękawy")
    g = int(input("Podaj liczbę garniturów do zrobienia: "))

    # Obliczenia dotyczące korpusów (poziom 2)
    k = g
    k_week_3 = g / 2

    # Obliczenia dotyczące rękawów (poziom 2)
    r = g * 2
    r_week_3 = g

    # Generowanie tabelki dla korpusów (poziom 2)
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 6):
        if week == 3:
            gross_requirements = k_week_3
            initial_inventory = k
            net_requirements = k_week_3 - k
            planned_receipt = k_week_3
        else:
            gross_requirements = 0
            initial_inventory = 0
            net_requirements = 0
            planned_receipt = 0

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")

    # Generowanie tabelki dla rękawów (poziom 2)
    print(f"\n+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 6):
        if week == 3:
            gross_requirements = r_week_3
            initial_inventory = r
            net_requirements = r_week_3 - r
            planned_receipt = r_week_3
        else:
            gross_requirements = 0
            initial_inventory = 0
            net_requirements = 0
            planned_receipt = 0

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")


def generate_level_three_table():
    # Poziom 3 - Wełna, Nić, Waterunek
    print("\nPoziom 3 - Wełna, Nić, Waterunek")
    g = int(input("Podaj liczbę garniturów do zrobienia: "))

    # Obliczenia dotyczące wełny (poziom 3)
    w = int(input("Podaj wstępny zapas wełny: "))
    net_wool = 2 * g

    # Obliczenia dotyczące nici (poziom 3)
    n = int(input("Podaj wstępny zapas nici: "))
    total_thread = g * 500

    # Obliczenia dotyczące waterunku (poziom 3)
    w1 = int(input("Podaj wstępny zapas waterunku: "))
    total_buttons = g * 2

    # Generowanie tabelki dla wełny (poziom 3)
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 2):
        gross_requirements = net_wool
        initial_inventory = w
        net_requirements = net_wool - w
        planned_receipt = net_wool

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")

    # Generowanie tabelki dla nici (poziom 3)
    print(f"\n+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 2):
        gross_requirements = total_thread
        initial_inventory = n
        net_requirements = total_thread - n
        planned_receipt = total_thread

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")

    # Generowanie tabelki dla waterunku (poziom 3)
    print(f"\n+--------+----------------+--------------+---------------+-----------------+")
    print(f"| Tydzień| Potrzeby brutto| Wstępny zapas| Potrzeby netto| Zaplanowany odbiór|")
    print(f"+--------+----------------+--------------+---------------+-----------------+")
    for week in range(1, 2):
        gross_requirements = total_buttons
        initial_inventory = w1
        net_requirements = total_buttons - w1
        planned_receipt = total_buttons

        print(f"|   {week}   |      {gross_requirements}        |     {initial_inventory}      |      {net_requirements}       |        {planned_receipt}       |")
    print(f"+--------+----------------+--------------+---------------+-----------------+")


def main():
    # Generowanie tabelki dla poziomu zero (garnitury)
    generate_level_zero_table()

    # Generowanie tabelki dla poziomu pierwszego (guziki)
    generate_level_one_table()

    # Generowanie tabelki dla poziomu drugiego (korpusy i rękawy)
    generate_level_two_table()

    # Generowanie tabelki dla poziomu trzeciego (wełna, nić, waterunek)
    generate_level_three_table()


# Uruchomienie głównej funkcji
main()
