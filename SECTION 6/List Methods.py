#---METHODS, AND THE LIST METHODS: Paginas 89 a 92 del libro--------------------------------------
#index(), append(), insert(), remove(), sort()

#Methods: El lo mismo que una funcion excepto que esta atado a un cierto valor.

#------------ #.index() = indice----------------------------------------------------------------------------
spam = ['hello', 'hi', 'howdy' , 'heyas']
x = spam.index('hello')                  
y = spam.index('hi')
a = spam.index('howdy')
b = spam.index('heyas')
#Con el spam.index(), es como si dijises: hey necesito encontrar donde
# esta alojado este string en la lista guardada en la variable spam.
print(x)
print(y)
print(a)
print(b)

print('///////////////////////////////////////////////////////////////////////')

#Si en la lista hay un string repetido, al usar la funcion index() va a llamar
#el primer string que encuentre que esta dentro de la lista.
spam = ['oe', 'hey', 'wa', 'hey']
p = spam.index('hey')
print(p)

#--------------append() and insert() List Methods----------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

#append() inserta un nuevo valor en la ultima parte de la lista.
spam = ['negro', 'rojo', 'azul', 'lila'] 
spam.append('rosa')
print(spam)

print('///////////////////////////////////////////////////////////////////////')

#insert() agrega un nuevo valor a la lista pero en cualquier parte (indice).
spam = ['hello', 'hi', 'howdy' , 'heyas']
spam.insert(1, 'yaaaa')
print(spam)

#los methods append() e insert() solo son metodos para listas y no se pueden llamar para enteros o strings.

#--------------------remove() List Method-----------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

#remove() remueve el valor dentro de la lista sin importar su ubicacion.
spam = ['A', 'B', 'C', 'D']
spam.remove('B')
print(spam)
#con remove especifica que valor remover es la diferencia con la funcion del() donde debe digitar el valor en que se encuentra el string.
print('///////////////////////////////////////////////////////////////////////')

#si en la lista hay valores repetidos solo se remueve el primer valor que se encuentre.
spam = ['D', 'E','D','F','D']
spam.remove('D')
print(spam)

#------------------sort() List Method-------------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

#sort() list method nos permite organizar los valores en orden.
spam = [2, 4, 3.14, 1 , -7]
spam.sort() #en orden numerico.
print(spam)

print('///////////////////////////////////////////////////////////////////////')

spam = ['xao', 'rat','octagonal', 'dude', 'aveline']
spam.sort() #en orden alfabetico.
print (spam)

print('///////////////////////////////////////////////////////////////////////')

spam = ['ant', 'badger', 'cat', 'dog', 'ellie']
spam.sort(reverse=True) #en orden alfabetico al contrario.
print(spam)

#sort() solo organiza strings, enteros, float individualmente, es decir que en la list solo haya un tipo de dato.

print('///////////////////////////////////////////////////////////////////////')

#----------ASCII-betical Order-----------------------------------------------------------------------------------------------

#Las palabras con letras mayusculas aparecen primero que las palabras con letras minusculas.

spam = ['Alice', 'Bob', 'ants', 'bad', 'cats', 'Carol']
spam.sort()
print(spam) #todas las letras mayusculas van primero que las minusculas

print('///////////////////////////////////////////////////////////////////////')

spam = ['A', 'Z', 'a', 'z']
spam.sort() 
print(spam) #todas las letras mayusculas van primero que las minusculas

print('///////////////////////////////////////////////////////////////////////')

spam.sort(key=str.lower) #key = str.lower es el argumento quwe nos permite hacerlo en orden alfabetico.
print(spam)















