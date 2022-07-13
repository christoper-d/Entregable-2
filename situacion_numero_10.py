
#                    -----IMPORT-----
#-  Eliminar si no se hace desde la termminal  O la CMD, junto a los clearConsole() del codigo
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
#-------------------------------------------------------------------------------------


#                 -----Main-----
#-------------------------------------------------------------------------------------
def main():
    try:
        print()
        print('-------------------------------')
        print('|    calcular los salarios    |')
        print('-------------------------------\n')

        print('      ---Bienvenido---     ')
        print()
        print('>Ingresa las horas:  \n')
        horas=int(input('=[> '))

        print('\n','                 '+'+--------------------------+')
        print(' >Ingrese el turno|   m   ||    t   ||   n   |  \n','                 '+'+--------------------------+')
        turno=input('=[>')
        salario=horas*37

        try: 
            if turno=="m":
                salario==horas*37
                if salario >=2000 and salario<=5000:
                    salario-=salario*0.15
                    print()
                    print("|       |El salario del trabajador es: ",salario)
                    print()
            elif turno=="t":
                salario+=salario*0.2
                if salario >=2000 and salario<=5000:
                    salario-=salario*0.15
                    print()
                    print("|       |El salario del trabajador es: ",salario)
                    print()
            elif turno=="n":
                salario+=salario*0.5  
                if salario >=2000 and salario<=5000:
                    salario-=salario*0.15
                    print()
                    print("|       |El salario del trabajador es: ",salario)
                    print()
        except:
            print('         ---vuelve a intentarlo xd---  \n')

    except:
        clearConsole() #Eliminar si no se hace desde la terminal
        print(' ')
        print('|       | ERROR: ¡ese es valor no valido! \n')
        print('         ---vuelve a intentarlo xd---  \n')
        main()
main()

#-------------------------------------------------------------------------------------
