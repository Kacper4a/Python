Unix = 1969
teraz = 2023
a = 365
b = 24
c= 60
lata = teraz - Unix
dni = lata * 365
godziny = dni * 24
minuty = godziny * 60
sekundy = minuty * 60

wyjscie = False
while wyjscie == False:

    print("::Menu::")
    print("1 Unix year")
    print("2 Unix Days")
    print("3 Unix Hours")
    print("4 Unix Minutes")
    print("5 Unix Seconds")
    print("6 Wyjscie")

    choice = input("Wybierz (1/2/3/4/5/6):")

    if choice == '6':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (1/2/3/4/5/6):")

    if choice == '1':
        print(teraz, "-", Unix, "=", lata)

    elif choice == '2':
        print(lata, "*", a, "=", dni,)

    elif choice == '3':
        print(dni, "*", b, "=", godziny)

    elif choice == '4':
        print(godziny, "*", c, "=", minuty)

    elif choice == '5':
        print(minuty, "*", c, "=", sekundy)

    else:
        print("Wybraleś nieistniejącą opcje!")
        
