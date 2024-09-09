'''
13) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Informe o valor a "))
b = int(input("Informe o valor b "))
c = int(input("Informe o valor c "))

# var a deve ser o menor de todos

if (a > b):
    aux = a
    a = b
    b = aux

if (a > c):
    aux = a
    a = c
    c = aux

if (b > c):
    aux = b
    b = c
    c = aux

print("A ordem crescente dos números apresentados é:")
print(a,b,c)