#Alfredo velasquez. P1E4. MAYOR DE DOS NUMEROS
n1 = int(input('Introduce 1 numero para ver el mayor entre el y el siguiente: '))
n2 = int(input('Introduce 1 numero para ver el mayor entre el y el anterior: '))

if n1>n2:
    print('El numero %d es mayor que el numero %d' % (n1, n2))
else:
    print('El numero %d es mayor que el numero %d' % (n2 ,n1))
