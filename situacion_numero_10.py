print()
print('-------------------------------')
print('|    calcular los salarios    |')
print('-------------------------------\n')

print('      ---Bienvenido---     ')

print()
print('>Ingresa las horas:  \n')
horas=int(input('=> '))

print()
print('>Ingrese el turno(m,t,n):  \n')
turno=input('=>')


salario=horas*37


if turno=="m":
    salario==horas*37
elif turno=="t":
    salario+=salario*0.2
elif turno=="n":
    salario+=salario*0.5

if salario >=2000 and salario<=5000:
    salario-=salario*0.15
elif salario>=8000 and salario<=10000:
    salario*=salario*0.17

print()
print("|       |El salario del trabajador es: ",salario)


#Autor: CHRISTOPER DIAZ© Año: 2022
