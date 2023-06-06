num1 = 42 #es la declaración de una variable con un tipo de dato: número entero
num2 = 2.3 #es la declaración de una variable con un tipo de dato: numero float
boolean = True #es la declaración de una variable con un tipo de dato: booleano
string = 'Hello World' #es la declaración de una variable con un tipo de dato: string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #es la declaración de una variable con un tipo de dato: array/arreglo
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #es la declaración de una variable con un tipo de dato:
fruit = ('blueberry', 'strawberry', 'banana') #es la declaración de una variable con un tipo de dato:array/arreglo
print(type(fruit)) #print es una función que permite mostrar en pantalla lo escrito en el código. En este caso imprimirá qué tipo de dato hay en la variable fruit.
print(pizza_toppings[1]) #en este caso se imprimirá gracias a 'print' el segundo elemento de la lista pizza_toppings, de una lista de elementos hechos en un arreglo/array (acordando que los elementos se enumeran como: 0,1,2,...)
pizza_toppings.append('Mushrooms') #append es una funcion que agregará un elemento al final de la lista del arreglo pizza_topings.
print(person['name']) #esta línea de código accede a los valores creados en un diccionario, en este caso imprimirá el valor de "name" del diccionario "person"
person['name'] = 'George' #en este caso se está asignando el valor "George" a la clave "name", del diccionario "person"
person['eye_color'] = 'blue' #se usa para asignar un valor a la clave de un diccionario.
print(fruit[2]) #se imprimirá en consola el tercer elemento de la lista "fruit"

if num1 > 45:                 #es una condicional if y else, que luego de leerse, se imprimirá en consola
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:            #es una condicional if, elif y else, que luego de leerse, se imprimirá en consola
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):             #es un bucle for y while, que luego de leerse, se imprimirá en consola
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()        #".pop" es una funcion que eliminará el último elemento de una lista
pizza_toppings.pop(1)       #en este caso ".pop(1)" eliminará el segundo elemento de una lista (acordando que los elementos se enumeran como: 0,1,2,...).

print(person)                
person.pop('eye_color')     #teniendo un diccionario de nombre "person", "person.pop" eliminará del diccionario la clave "eye_color".
print(person)               #Luego se imprimirá en pantalla nuevamente con la funcion "print"

for topping in pizza_toppings:      #es un bucle con condicionales if
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():        #def se usa para definir una función. En este caso esta función llamada "print_hello..."
    for num in range(10):           #tiene un bucle for que se repetirá 10 veces de 0 a 9
        print('Hello')              #imprimiendo la palabra "hello" 10 veces en consola

print_hello_ten_times()             #es llamar a una función, que imprimirá el código que se haya creado en la función "print_hello_ten_times"

def print_hello_x_times(x):         #definir esta función toma como argumento el "x", y que luego imprimirá "x" veces en la consola
    for num in range(x):
        print('Hello')

print_hello_x_times(4)              #esta llamada de función, repetirá 4 veces el bloque de código creado dentro de la función "print_hello_x_times"

def print_hello_x_or_ten_times(x = 10): #definir esta función toma como argumento el "x", pero con un valor de 10. el bucle imprimirá 
    for num in range(x):                #10 veces "Hello". si se llama a la función por otro valor, se imprimirá por esa cantidad de veces.
        print('Hello')

print_hello_x_or_ten_times()            #se llama a la función con un valor determinado, que es 10, porque x es 10.
print_hello_x_or_ten_times(4)           #se llama a la función con un valor de 4, por lo que se imprimirá Hello 4 veces.


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)