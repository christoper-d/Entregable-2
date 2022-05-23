#1.	Escribe un programa que solicité al usuario ingresar cuatro números para luego mostrar el promedio de los cuatro.

###puedes escoger caulquiera de las dos formas###

############= PRIMERA FORMA =############

print('forma 1')#forma1
a = 4
total = 0

print()
print('--------------------------')
print('|  >Ingrese sus numeros  |')
print('--------------------------\n')

for i in range(a):
    b=int(input('=> '))
    total = total+b

print()
print(f'El promedio es: {total/a}')
print()

############= SEGUNDA FORMA =############

print('forma 2')#forma2

a=int(input('ingrese su numero > '))+int(input("ingrese su numero > "))+int(input("ingrese su numero > "))+int(input("ingrese su numero > 3"))
print(a)


# Autor: CHRISTOPER SANCHEZ DIAZ©   año:2022
