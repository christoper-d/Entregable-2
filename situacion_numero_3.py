

#--------Datos del empleado
name= 'christoper'#input('')
workhours=12#int(input(''))
salary=5#int(input(''))
#--------------------------


#--------------------------------- Salida de los datos del empleado
print()
print('--- Empleados ---')
print()
empleado = {
    'Nombre':name,
    'Horas de trabajo':workhours,
    'Salario por hora':salary,
}
print(' • Empleado 1 :')
print()
print('     ->','\n     -> '.join("{}: {}".format(k, v) for k, v in empleado.items()))
print(' \n',' \n')



#--------Salario variables---------
#--------SALARIO NORMAL
UN_DIA = (empleado["Horas de trabajo"]*empleado["Salario por hora"])
UNA_SEMANA = (7*(UN_DIA))
UN_MES = (4*UNA_SEMANA)
UN_AÑO = (12*UN_MES)
#----------------------

#--------SALARIO + 15%
newsalary = salary+((15/100)*salary)

empleado['Salario por hora']=newsalary
#---------Salario aumentado
UN_DIAMAS = (empleado['Horas de trabajo']*empleado['Salario por hora'])
UNA_SEMANAMAS = (7*UN_DIAMAS)
UN_MESMAS = (4*UNA_SEMANAMAS)
UN_AÑOMAS = (12*UN_MESMAS)
#--------------------------
#------------------------------------


#---------------------------------Salida
print('--- Salario Normal ---')
print()
print('+----------------------------------------------------------+')
print('|          | [Un dia] | [Una semana] | [Un mes] | [un año] |')
print('+----------|----------|--------------|----------|----------+')
print(f'|Sueldo    |   {UN_DIA}\S   |     {UNA_SEMANA}\S    |  {UN_MES}\S  | {UN_AÑO}\S  |')
print('+----------|----------|--------------|----------|----------+')
print()
print()
print('--- Salario + 15% ---')
print()
print('+----------------------------------------------------------------+')
print('|               | [Un dia] | [Una semana] | [Un mes] | [un año]  |')
print('+---------------|----------|--------------|----------|-----------+')
print(f'|Sueldo + 15%   |  {UN_DIAMAS}\S  |    {UNA_SEMANAMAS}\S   | {UN_MESMAS}\S | {UN_AÑOMAS}\S |')
print('+---------------|----------|--------------|----------|-----------+')
print()
#------------------------------------------



#Autor: CHRISTOPER SANCHEZ DIAZ©   año:2022
