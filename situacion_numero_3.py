import json
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()   
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

print('\n'.join("{}: {}".format(k, v) for k, v in empleado.items()))

print(json.dumps(empleado, sort_keys=False, indent=4))
print('un dia de trabajo: ',empleado['Horas de trabajo']*empleado['Salario por hora'], 'soles')
print('una semana de trabajo: ',7*(empleado['Horas de trabajo']*empleado['Salario por hora']), 'soles')
print('un mes de trabajo: ',4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora'])), 'soles')
print('un año de trabajo: ',12*(4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora']))), 'soles')


#########################
print('felicicitacionesse te subieron el sueldoen un 15%')
print('Deseas actualizar para ver los cambios?')

print('si(s) o no(n)')
accion=input('> ')
if accion == 's':
    clearConsole()
##########################

newsalary = salary+((15/100)*salary)

empleado['Salario por hora']=newsalary

print('*New actualizacion de salario*')

print('un dia de trabajo: ',empleado['Horas de trabajo']*empleado['Salario por hora'], 'soles')
print('una semana de trabajo: ',7*(empleado['Horas de trabajo']*empleado['Salario por hora']), 'soles')
print('un mes de trabajo: ',4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora'])), 'soles')
print('un año de trabajo: ',12*(4*(7*(empleado['Horas de trabajo']*empleado['Salario por hora']))), 'soles')

#Autor: CHRISTOPER SANCHEZ DIAZ©   año:2022
