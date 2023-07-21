#Actividad nº1
# n = 0
# def anio_bisiesto(n):
#     try:
#         n = int(input("Ingrese año: "))
#         if n%4 == 0 or n%400 == 0:  
#             print(f'Año bisiesto:'.upper(),n)
#         else:
#             print('No es año bisiesto'.upper())
#     except ValueError:
#         print('No válido, ingrese año'.upper())
            
# anio_bisiesto(n)

#Actividad nº2
# 1)
# a = float(input("altura: "))
# b = float(input("base: "))
# def area_rectangulo(a,b):
#     return a*b
# resultado = area_rectangulo(a,b)
# print(f'Área del rectángulo= {resultado:.1f}')

# 2)

# import math
# r = float(input("radio= "))
# def area_circulo(r):
#     return math.pi*r**2
# resultado = area_circulo(r)
# print(f'Área del circulo= {resultado:.1f}')

# 3)

# x = float(input("x = "))
# y = float(input("y = "))
# def compara_numero(x,y):
#     if x > y:
#         return 1
#     elif x < y:
#         return -1
#     elif x == y:
#         return 0
# resultado = compara_numero(x,y)
# print("resultado de comparar X y Y: ",resultado)

# 4)

# x = float(input("x = "))
# y = float(input("y = "))
# def valor_intermedio(x,y):
#     return (x + y)/2
# resultado = valor_intermedio(x,y)
# print(f"valor intermedio entre X y Y: {resultado:.1f}")

# 5)


# a = int(input("numero_a: "))
# b = int(input("número_b: "))
# c = int(input("número_c: "))
# def recortar (a,b,c):
#     if b < c:
#         if  a in range(b, c+1):
#             return print("inferior:",b, "\nmaximo: ",c)
#         elif a > c:
#             return print("inferior:", c)
#         elif a < b:
#             return print("superior:", b)          
#     else:
#         if a < c:
#             return(print("maximo:", c))
#         elif a > b:
#             return(print("minimo:", b))
# recortar(a,b,c)

# 6)

# a)
# n = int(input("n = "))
# lista = []
# def separar():
#     if n > 0:
#         for i in range(1,n+1):
#             lista.append(i)  
#             lista_par = []
#             lista_impar = []
#             for i in lista:
#                 if i%2 == 0:
#                     lista_par.append(i)
#                 else:
#                     lista_impar.append(i)
#         print(f'lista:',lista, '\nlista impar:',lista_impar, '\nlista impar:',lista_par)
# separar()

# b)

# lista = [13, 4, 6, 7, 15, 24, 11]
# def separar():  
#     lista_par = []
#     lista_impar = []
#     for i in lista:
#         if i%2 == 0:
#             lista_par.append(i)
#             lista_par.sort()
#         else:
#             lista_impar.append(i)
#             lista_impar.sort()
#     print(f'lista:',lista, '\nlista impar:',lista_impar, '\nlista impar:',lista_par)
# separar()

