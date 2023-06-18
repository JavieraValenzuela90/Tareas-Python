for count in range(0,5):
    print("looping =", count)

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

def sumar(a,b):
    return a + b

resultado = sumar(3,2)
print(resultado)

def casa(nombre):
    return "Hola " + nombre

bienvenida = casa("Javi")
print(bienvenida)

def colegio(alumno):
    return "Bienvenid@ " + alumno

primer_dia = colegio("Javi")
print(primer_dia)


def multiplicar(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)

