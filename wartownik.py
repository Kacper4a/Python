from random import randint

howManyNumbers = 10  # rozmiar tablicy
startNum = 0  # minimalna wartosc elementu
endNum = 100  # maksymalna wartosc elementu
guard = ""
arr = [1]

# wypelnij tablice przypadkowymi wartosciami
for i in range(howManyNumbers):
    arr.append(randint(startNum, endNum))

while True:
    try:
        findNum = int(input("Guess a number: "))  # odgadnij liczbe
    except ValueError:
        print("It's not a number !!! Try again.")  # nie podano liczby
    else:
        arr.append(findNum)  # dodaj wartownika do tablicy
        i = 0
        while arr[i] != findNum:  # dopoki nie znaleziono elementu
            i += 1  # przesuwaj sie dalej
        break

if i == howManyNumbers:
    print("Guard! Number not exist.")  # znalzeiono wartownika, szukana liczba nie znajduje sie w tablicy
else:
    print("Number has been founded: ", str(findNum), "on index", i)  # znaleziono podana liczbe pod indexem i

# wait before close console application
input("Press enter to exit.")