#for LOOPS


#Itera un numero especifico de veces.
print('My name is')
for i in range (5):
    print ('Jimmy Five Times '+ str (i))



#Sumatoria de los primeros 100 numeros Ejemplo de Gauss
total = 0
for num in range (101):
    total = total + num
print(total)



# range() function
print('My name is')
for i in range (12, 16):   
    #Dos argumentos en el range 12 donde inicia el for y 16 donde acaba sin incluir ese valor
    print ('Jimmy Five Times '+ str (i))


print('My name is')
for i in range (0, 10, 2):   
    #Tres argumentos en el range 12 donde inicia el for y 16 donde acaba sin incluir ese valor
    #El argumento 2 es la cantidad con la que aumenta en ese rango.
    print ('Jimmy Five Times '+ str (i))


print('My name is')
for i in range (5,-1,-1):
    #se usan numeros negativos para contar de mayor a menor.
    print ('Jimmy Five Times '+ str (i))



#break and continue pueden usarse en estos loops
for letter in 'Django':    
    if letter == 'D':
        continue
    print("Current Letter: " + letter)