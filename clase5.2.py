# Práctica Métodos y Ayuda 1
# Remueve los caracteres a la izquierda de nuestro texto principal:

# ,

# :

# %

# _

# #

# Utiliza el método lstrip(). Imprime el resultado en pantalla:
# texto = (",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))
# resultado = texto.lstrip
# print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.



# Práctica Métodos y Ayuda 2
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

# el método insert():

# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
# frutas.insert(3,"naranja")
# print(frutas)

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.


# Práctica Métodos y Ayuda 3
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
# conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
# print(conjuntos_aislados)

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento




# Funciones Propias

# def mi_funcion():
#     '''esta funcion se encarga de 
#     imprimir un saludo en pantalla'''
#     print("hola luciano")

# mi_funcion()

# def mi_funcion(nombre):
#     """ esta funcion se encarga de 
#     imprimir un saludo en pantalla"""
#     print(f"hola {nombre}")


# mi_funcion("luis")


# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

# Solo debes definir la función, no debes invocarla luego.

def saludar():
    print("¡Hola mundo!")

# Práctica Crear Funciones 2
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

# Solo debes definir la función y crear la variable, no debes invocar la función luego.

# def bienvenida(nombre_persona):
#     nombre_persona = Marcela
#     print (f"Bienvenida{nombre_persona}")


# Práctica Crear Funciones 3
 #Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

# Solo debes definir la función y crear la variable, no debes invocar la función luego.

# def cuadrado (un_numero):
#     un_numero = 5
#     print((un_numero**2))


# # Return 

# def multiplicar(numero1,numero2):
#     total = numero1 * numero2
#     return total

# resultado = multiplicar(5,200)
# print(resultado)

# Práctica Return 1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:


# def potencia(base,exponente): 
#     return base**exponente
# base = 12
# exponente = 2


# Práctica Return 2
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

# Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.

# def usd_a_eur(dolares):
#     dolares = 250
#     return dolares*0.90


# Práctica Return 3
# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

# Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

# También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

# Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

# def invertir_palabra(palabra):
#     return palabra[::-1].upper()
# palabra = "mariposa"



# def chequear_3_cifras(lista):


    
#     for n in lista:
#         if n == range(100,1000):
#             return True
#         else:
#             continue
#     return False
    

# resultado = chequear_3_cifras([555,99,600])
# print(resultado)

# def chequear_3_cifras(lista):
#     lista_3_cifras =[]
#     for n in lista:
#         if n == range(100,1000):
#             lista_3_cifras.append(n)
#         else:
#             continue
#     return lista_3_cifras

# resultado = chequear_3_cifras([555,99,600])
# print(resultado)


# Práctica Funciones Dinámicas 1
# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

# No invoques la función, solo es necesario definirla.

# def todos_positivos(lista_numeros):
#     for numero in lista_numeros:
#         if numero < 0 :
#             return False
#     return True

# lista_numeros = [2,5,-3,8,6,-7]

# Práctica Funciones Dinámicas 2
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

# def suma_menores(lista_numeros):
#     suma = 0
#     for numero in lista_numeros:
#         if 0 < numero > 1000 :
#             suma += numero
#     return suma

# lista_numeros = [5,63,578,2030,181]


# Práctica Funciones Dinámicas 31

# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

# def cantidad_pares(lista_numeros):
#     suma = 0
#     for numero in lista_numeros:
#         if numero / 2 == 0:
#             suma += 1
#             return numero
#         return suma

# lista_numeros = [2,9,5,4,3,6]



# precios_cafe = [("capuchino",1.5), ("Expresso",2.5), ("Moka",3.5)]

# def cafe_mas_caro(lista_precios):

#     precio_mayor = 0
#     cafe_mas_caro = ''

#     for cafe,precio in lista_precios:
#         if precio > precio_mayor:
#             precio_mayor = precio_mayor
#             cafe_mas_caro = cafe
#         else:
#             pass
#     return(cafe_mas_caro,precio_mayor)

# cafe, precio = cafe_mas_caro(precios_cafe)
# print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")



# from random import shuffle

# # lista inicial 
# palitos = ['-','--','---','----']
# # mezclar palitos 
# def mezclar(lista):
#     shuffle(lista)
#     return lista

# # pedirle intento
# def probar_suerte():
#     intento = ''
#     while intento not in ['1','2','3','4']:
#         intento = input("Elige un numero del 1 al 4: ")
#     return int(intento)
# # Comprobar intento 
# def chequear_intento(lista, intento):
#     if lista[intento - 1] == '-':
#         print("Te toco el 8")
#     else:
#         print("Te has salvado ")
    
#     print(f"Te ha tocado {lista[intento-1]}")

# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)



# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buenas chances"

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.

# import random

# def lanzar_dados():
#     dado_1 = random.randint(1,6)
#     dado_2 = random.randint(1,6)
#     return dado_1,dado_2

# def evaluar_jugada(dado_1,dado_2):
#     suma_dados = dado_1 + dado_2
#     if suma_dados <=6:
#         return f"La suma de tus dados es {suma_dados}. Lamentable."
#     elif suma_dados >=7 < 10:
#         return f"La suma de tus dados es {suma_dados}. Tienes buenas chances."
#     elif suma_dados >= 10:
#         return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora."
    
#     resultado_dados = lanzar_dados()
#     mensaje = evaluar_jugada(*resultado_dados)


# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

# def reducir_lista(lista):
#     eliminar_duplicados = list(set(lista))
#     eliminar_duplicados.remove(max(eliminar_duplicados))
#     return eliminar_duplicados

# def promedio(lista):
#     return sum(lista) / len(lista) if lista else 0

# lista_numeros = [1,2,15,7,2]
 
# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

# import random

# def lanzar_moneda():
#     return random.choice(["Cara", "Cruz"])

# def probar_suerte(resultado, lista_numeros):
#     if resultado == "Cara":
#         print(f"La lista se autodestruirá")
#         return[]
#     else:
#         print("La lista fue salvada")
#         return lista_numeros

# lista_numeros = [5,6,9,12,4,25]


# def mi_funcion( *args):
#     return sum(args)

# resultado = mi_funcion(1,2,40,50)
# print(resultado)



# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

# def suma_cuadrados(*args):
#     return sum(x ** 2 for x in args)
# resultado = suma_cuadrados(4,3,2)
# print(resultado)


# Práctica sobre Argumentos Indefinidos (*args) 2

# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

# def suma_absolutos(*args):
#     return sum(abs(x) for x in args)
# resultado = suma_absolutos(4,-5,2,-3)
# print(resultado)


# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje:

# "{nombre}, la suma de tus números es {suma_numeros}"

# def numeros_persona(nombre, *numeros):
#     suma_numeros = sum(numeros)
#     return f"{nombre}, la suma de tus números es {suma_numeros}"

# print(numeros_persona("Mara", 4,5,7))


# def suma  (**kwargs):
#     total = 0
#     for clave,valor  in kwargs.items():
#         print(f"{clave} = {valor}")
#         total += valor

#     return total



# print(suma(a=1,b=2,c=3))


# def test(num1,num2,*args,**kwargs):

#     print(f"el primer valor es {num1}")
#     print(f"el segundo valor es {num2}")

#     for arg in args:
#         print(f"arg = {arg}")
    

#     for clave,valor in kwargs.items():
#         print(f"{clave} = {valor}")

# args = [100,200,300,400]


# test(20,10,100,200,300,400,a=1,b=2,c=3)


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

# def cantidad_atributos(**kwargs):
#     return len(kwargs)

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

# def lista_atributos(**kwargs):
#     return list(kwargs.values())

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio

# Características de Bruno:
# estatura: alto
# pelo: rizado
# color_pelo: rubio
# color_ojos: marrones
# atributo: simpático

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona("Bruno",estatura="alto",pelo="rizado", color_pelo="rubio",color_ojos="marrones",atributo="simpatico")
