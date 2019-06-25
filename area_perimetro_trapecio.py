#Calcular el area y perimetro de un trapecio

def areatrapecio(Base, base, altura):
    Areatrapecio=((Base+base)*altura)/2
    return Areatrapecio

def perimtrapecio(Base, base, lado1, lado2):
    Perimtrapecio=Base+base+lado1+lado2
    return Perimtrapecio

B=float(input("Introduzca el valor de la base mayor: "))
b=float(input("Introduzca el valor de la base menor: "))
h=float(input("Introduzca el valor de la altura: "))
l1=float(input("Introduzca el valor del lado 1: "))
l2=float(input("Introduzca el valor del lado 2: "))
A=areatrapecio(B, b, h)
P=perimtrapecio(B, b, l1, l2)

print("El area del trapecio es: ", A,"\nEl perimetro del trapecio es: ", P)