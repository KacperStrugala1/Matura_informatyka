
def dzieliniki_liczby(liczba):

    for x in range(1,int(liczba+1)):
        if liczba % x == 0:
            print(str(x) + " ")
        else:
            continue

a = int(input("Podaj liczbe: "))
dzieliniki_liczby(a)