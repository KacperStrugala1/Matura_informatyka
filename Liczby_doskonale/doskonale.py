
def doskonale(a):
    suma = 0
    iloczyn = 1
    for x in range(1,(int(a/2)+1)):
        if a % x == 0:
            print(str(x) + " ")
            suma += x
            iloczyn *= x
        else:
            continue
    if suma == a:
        print(f"Liczba jest doskonala: \nSuma: {suma}")
    else:
        print("Liczba nie jest doskonala 1 stopnia")
    if iloczyn == a:
                print(f"Liczba jest doskonala 2 stopnia, iloraz: {iloczyn}")
    else:
        print("Liczba nie jest doskonala 2 stopnia")





a = int(input("Podaj liczbe: "))
doskonale(a)
