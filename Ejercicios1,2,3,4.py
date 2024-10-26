#Ejercicio 1

# def devolver_distintos(a, b, c):
    
#     suma = a + b + c
#     if suma < 15:
#         return max(a, b, c)
#     elif suma < 10:
#         return min(a, b, c)
#     else:
#         numeros = [a, b, c]
#         numeros.sort()
#         return numeros [1]
    
# resultado = devolver_distintos(14, 3 ,1)  

# print(f"El número mayor es: {max(14, 3, 1)} ")
# print(f"El número menor es: {min(14, 3, 1)} ")
# print(f"El número intermedio es: {resultado} ")




#Ejercicio 2

# def letras_ordenadas(palabra):
#     letras = set(palabra)
#     letras_ordenadas = sorted(letras)
#     return letras_ordenadas
# resultado = letras_ordenadas("pensamiento")
# print(f"{resultado}")


#Ejercicio 3

# def tiene_ceros(*args):
#     for i in range (len(args)-1):
#         if args[i] == 0 and args [i+1] == 0:
#          return True
#     return False
# print(tiene_ceros(3,2,0,0,5,8,7))
# print(tiene_ceros(4,2,5,0,1,2))


   #Ejercicio 4 
        
# primos = []
# input = int(input('Ingrese un número => '))
# def es_primo(k):
#     for i in range(2,k):
#         if (k % i) == 0:
#          return False
#     return True

# def contar_primos(n):
#     numeros = range(2,n)
#     for p in numeros:
#       if es_primo(p):
#             primos.append(p)
#     if es_primo(n):
#         primos.append(n)
#         print(f'El número {n} es primo.')
#     else:
#         print(f'El número {n} no es primo.')
#     if len(primos)!=0:
#             print(f'La lista de números primos en el rango es: {primos}')

# contar_primos(input)

        




