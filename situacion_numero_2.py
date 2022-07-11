#contribuciones
juan = 6090
carlos = 4435
maria = 2299

#total de lo recaudado
empresa =(juan+carlos+maria)


#operacion para sacar el porcentaje
porcentaje =((juan/empresa)*100)
porcentaje2 =((carlos/empresa)*100)
porcentaje3 =((maria/empresa)*100)

#total de los porcentajes
total=(porcentaje+porcentaje2+porcentaje3)


##salida##
print()
print('######### sin resolver ########\n')

print('----------------------------')
print(f'|Personas|dinero|Porcentaje|')
print('----------------------------')
print(f'|JUAN   |  {juan}  |  ?  |')
print(f'|CARLOS |  {carlos}  |  ?  |')
print(f'|MARIA  |  {maria}  |  ?  |')
print('*---------------------------')
print(f'| Total:| {empresa}  | {round(total)} %   |')
print('*---------------------------\n')

print('######### RESUELTO ########\n')

print('----------------------------')
print(f'|Personas|dinero|Porcentaje|')
print('----------------------------')
print(f'|JUAN   |  {juan}  |  {round(porcentaje)} %   |')
print(f'|CARLOS |  {carlos}  |  {round(porcentaje2)} %   |')
print(f'|MARIA  |  {maria}  |  {round(porcentaje3)} %   |')
print('*---------------------------')
print(f'| Total:| {empresa}  | {round(total)} %   |')
print('*---------------------------')


#Autor: CHRISTOPER DIAZ©   año:2022
