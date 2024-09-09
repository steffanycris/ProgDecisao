'''
12) Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.
'''

n1 = int(input("Informe a primeira nota "))
n2 = int(input("Informe a segunda nota "))
n3 = int(input("Informe a terceira nota "))
n4 = int(input("Informe a quarta nota "))
n5 = int(input("Informe a quinta nota "))

maior = num1
maior = num2 if num2 > maior else maior
maior = num3 if num3 > maior else maior
maior = num4 if num4 > maior else maior
maior = num5 if num5 > maior else maior

menor = num1
menor = num2 if num2 < menor else menor
menor = num3 if num3 < menor else menor
menor = num4 if num4 < menor else menor
menor = num5 if num5 < menor else menor

print("O menor valor é ",menor)
print("O maior valor é",maior)
