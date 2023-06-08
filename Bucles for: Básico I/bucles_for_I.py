
for i in range(151):
    print(i)

for i in range(0,1001,5):
    print(i)

for i in range(101):
    if (i % 5 == 0) or (i % 10 == 0):
        if (i % 5 == 0):
            print("Coding")
        if (i % 10 == 0):
            print("Coding Dojo")
    else:   
        print(i)

suma = 0
for i in range(1, 500001, 2):
    suma += i

print(suma)

for i in range(2018, 0, -4):
    print(i)

lowNum = 1
highNum = 20
mult = 2
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)




