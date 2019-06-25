#Calcular el area y perimetro de un triangulo
def areatriangulo(base, altura):
    Areatriangulo=(base*altura)/2
    return Areatriangulo

def perimtriangulo(lado):
    Perimtriangulo=lado*3
    return Perimtriangulo

b=float(input("Inserte el valor de la base del triangulo: "))
a=float(input("Inserte el valor de la altura del tringulo"))
A=areatriangulo(b, a)
P=perimtriangulo(b)
print("El area del triangulo es: ", A,"\nEl perimetro del triangulo es: ", P)