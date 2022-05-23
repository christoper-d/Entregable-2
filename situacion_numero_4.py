print()
print('--------------------------')
print('|  >Ingrese sus numeros  |')
print('--------------------------\n')

num1 =float(input('=> '))
num2 =float(input('=> '))

print()
print('*-----------------------------')
print('|   Operaciones Disponibles  |')
print('*-----------------------------')
print('|SUMA           |  1  |')
print('|RESTA          |  2  |')
print('|MULTIPLICACION |  3  |')
print('|DIVISION       |  4  |')
print('*-----------------------------\n')

print('¿Que operacion desea realisar?\n')
accion=int(input('> '))

def imprimir_resultado(accion):
    if accion == 1:
        print()
        print('*-------------------------------')
        print(f'| Resultado: | "{num1+num2}" o "{round(num1+num2)}" |')
        print('*-------------------------------\n')
    elif accion == 2:
        print()
        print('*-------------------------------')
        print(f'| Resultado: | "{num1-num2}" o "{round(num1-num2)}" |')
        print('*-------------------------------\n')
    
    elif accion == 3:
        print()
        print('*-------------------------------')
        print(f'| Resultado: | "{num1*num2}" o "{round(num1*num2)}" |')
        print('*-------------------------------\n')
    
    elif accion == 4:
        print()
        print('*-------------------------------')
        print(f'| Resultado: |"{num1/num2}" o "{round(num1/num2)}" |')
        print('*-------------------------------\n')

imprimir_resultado(accion)

#Autor: CHRISTOPER SANCHEZ DIAZ©   año:2022
