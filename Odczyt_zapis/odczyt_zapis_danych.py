
with open("zarobki.txt") as f:
    data = []
    pensja = 0.0
    suma = 0
    for line in f:
        splitted_line = line.split()

        miesiac = splitted_line[0]
        pensja = float(splitted_line[1])
        print(f"{miesiac} - pensja: {pensja}")

        suma += pensja
        print(f"Suma: {suma:.2f}")

with open("suma.txt", 'w')as n:
    n.write(f"Suma zarobkow: {suma:.2f}")