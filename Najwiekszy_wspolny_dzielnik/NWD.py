def nwd(x,y):
    z = x % y if(x > y) else y % x
    if z == 0:
        return y if (x > y) else x
    return nwd(z,y) if x>y else nwd(z,x)

print("Podaj a: ")
a = int(input())
print("Podaj liczbe b:")
b = int(input())
print(nwd(a,b))