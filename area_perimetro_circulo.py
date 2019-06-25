#Calcular area y perimetro de un circulo
pi=3.1415
def areacirculo(radio):
    Areacirculo=pi*(radio**2)
    return Areacirculo

def perimcirculo(radio):
    Perimcirculo=(2*pi)*radio
    return Perimcirculo

r=float(input("Introduce el valor del radio: "))
A=areacirculo(r)
P=perimcirculo(r)
print("El area del circulo es: ", A,"\nEl perimetro del circulo es: ", P)