#WRITING FUNCTIONS


#Ejemplo 1

def hello():              #def statement para definir una nueva funcion
    print ('Howdy!')             #
    print ('Howdy!!!')           # Estas tres son el bloque (cuerpo)
    print ('Hello there.')       # de la funcion definida

hello()                    #aqui llamamos la funcion por lo que
hello()                    # la funcion aparece 3 veces al ejecutar
hello()                    #el programa


#Ejemplo 2

def n(name):      
#name es un parametro = La variable dentro de la funcion n.
          
    print('Hello '+ name)

n('Alice')  #'Alice' string es un argumento 
n('Andres') #'Andres' string es un argumento 

#Los argumentos queda asignados al parametro n
# y luego se ejecuta el codigo dentro de la funcion .



#Return Statements

#Ejemplo 1
def plus(number):        # 1. define  la funcion plus(number)
    return number + 1    # 3. El valor que esta expresion evalua sera el valor retornado en esta funcion.
newnumber = plus(5)      # 2. La variable newnumber = plus(5). El valor es 5.
print (newnumber)        # 4. Imprime la variable newnumber. Imprime el 6 el valor evaluado en la expresion.

#Ejemplo 2






#The None Value



#Keyword Arguments (Opcionales)

#Ejemplo 1

print('Hello')
print('World')

print('Hello ', end = '')
print('World')

#Ejemplo 2
print('cat', 'dog', 'mouse')

print('cat', 'dog', 'mouse', sep= 'ABC')











