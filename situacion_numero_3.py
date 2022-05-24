#########################
    
name= 'christoper'#input('')
workhours=12#int(input(''))
salary=5#int(input(''))

#########################

empleado = {
    'Nombre':name,
    'Horas de trabajo':workhours,
    'Salario por hora':salary,
}
print('=[> Empleado:')
print()
print('      ','\n       '.join("{}: {}".format(k, v) for k, v in empleado.items()))
print(' \n',' \n')

print('|       |>un dia de trabajo: ',empleado['Horas de trabajo']*empleado['Salario por hora'], 'soles')
print('|       | >una semana de trabajo: ',7*(empleado['Horas de trabajo']*empleado['Salario por hora']), 'soles')
print('|       |  >un mes de trabajo: ',4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora'])), 'soles')
print('|       |   > un año de trabajo: ',12*(4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora']))), 'soles')


#########################
print()
print('---------felicicitacionesse te subieron el sueldoen un 15%----------')

##########################

newsalary = salary+((15/100)*salary)

empleado['Salario por hora']=newsalary
print()
print('-------*New actualizacion de salario*-------')
print()
print('|       |>un dia de trabajo: ',empleado['Horas de trabajo']*empleado['Salario por hora'], 'soles')
print('|       | >una semana de trabajo: ',7*(empleado['Horas de trabajo']*empleado['Salario por hora']), 'soles')
print('|       |  >un mes de trabajo: ',4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora'])), 'soles')
print('|       |   >un año de trabajo: ',12*(4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora']))), 'soles')

#Autor: CHRISTOPER SANCHEZ DIAZ©   año:2022
