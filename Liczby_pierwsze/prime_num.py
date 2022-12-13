




import math
def prime(a):
    if a < 2:
        return False
    for x in (range(2,int(a))):
        if a % x == 0:
            return False

    return True


a = int(input("Podaj liczbe: "))

print(prime(a))















'''
import math
def czyPierwsza(a):
    if a < 2:
        return False
    for i in (range(2, int(a))):
        if a % i == 0:
            return False
    return True


print("Program sprawdzający, czy liczba jest liczbą pierwszą.")
print("Podaj liczbę: ")
a = int(input())
print(czyPierwsza(a))
'''