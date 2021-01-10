#---------------------------------THE LIST DATA TYPE LESSON--------------------------------------------------

#A list is a value that contains multiple values in an ordered secuence.
#List's values = items
#begin and ends with the []
#comma delimited ,

#Ejemplo: ['cat', 'bat', 'rat','elephant']


x = ['cat','bat','rat','elephant']
print(x)
print(x[0], x[1], x[2], x[3] )

print('///////////////////////////////////////////////////////////////////////')

y = [['uy','tas'], [10, 20, 30, 40, 50]]
print(y[0])
print(y[0][1])

print(y[1])
print(y[1][3])

#---------------------------negative indexes-------------------------------------------------------

print('///////////////////////////////////////////////////////////////////////')

z = ['cat','bat','rat','elephant']
print(z[-1])
print(z[-1], z[-2], z[-3], z[-4])
#se pueden concatenar.
print('The '+ z[-1] + ' is afraid of the '+ z[-3] + '.')



#----------------------------------slice-----------------------------------------------------------------                                                      
#  index = single value
#se puede obtener distintos items de una lista.              slice = list of values
print('///////////////////////////////////////////////////////////////////////')

u = [90, 50, 63, 10]
print(u[1:3])


#-------------------------------changing list's items.-------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

b = [10, 20, 30]
b[1] = 'Hello'        #Se cambia el 20 por el Hello.
print(b)

b[1:3] = ['A', 'B', 'C']
print(b)


#------------------------------------slice shortcuts---------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

c = ['ti','ger','hat','phant']
c[:2]        #El espacio en blanco lo toma como si comenzara desde cero.
print(c[:2])   

c[1:]   #El espacio en blanco lo toma como el ultimo de la lista. Toma el ultimo de la lista.
print(c[1:])



#------------------------Delete Statements------------------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

#se usa la funcion delete del. Elimina items de la lista.

k = ['dog','bat','tiger','elephant']
del k[2]  #Elimina tiger
print(k)
del k[2]  #Elimina elephant
print(k)

#-----------------------------String and list similarities-------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

p = [1, 2, 3]
q = [4, 5, 6]
print(len(p)) #Se usa la funcion len para decir que cantidad de elementos hay en la lista.


print(p + q) #Se puede hacer concatenacion de listas
print(p * 3) #Se puede replicar listas

#--------------------------------------Funcion list()-------------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

print(list('Hello'))

#----------------------------------The in and not in Operators-------------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

f = ['hello', 'hi', 'howdy', 'ya']

print('howdy' in f)
print('cat' in f)
print('howdy'not in f)






































 




