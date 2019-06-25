#Calcular el area y perimetro de un cuadrado
def areacuadrado(lado):
    Areacuadro=lado*lado
    return Areacuadro

def perimcuadrado(lado):
    Perimcuadro=lado*4
    return Perimcuadro

l=float(input("Inserte el valor del lado del cuadrado: "))
A=areacuadrado(l)
P=perimcuadrado(l)
print("El area del cuadrado es: ", A,"\nEl perimetro del cuadrado es: ", P)