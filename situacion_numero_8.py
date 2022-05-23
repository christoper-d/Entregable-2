print()
print('---------------------------')
print('|    VERIFICDOR DE DNI    |')
print('---------------------------\n')

print('      ---Bienvenido---     ')

print()
print('>Ingresa tu DNI  \n')


DNI =input('=> ')
contador = 0

for x in DNI:
    contador+=1

print()
if contador > 8:
    print(f'|       | DNI contiene más de 8 caracteres\n')
elif contador < 8:
    print(f'|       | DNI contiene menos de 8 caracteres\n')
else:
    print(f'|       | El DNI es correcto\n')
