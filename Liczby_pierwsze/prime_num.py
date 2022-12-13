
def prime(a):
    if a < 2:
        return False
    for x in (range(2,int(a))):
        if a % x == 0:
            return False

    return True


a = int(input("Podaj liczbe: "))

print(prime(a))
