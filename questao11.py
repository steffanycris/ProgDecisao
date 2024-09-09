'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

num = int(input("Informe um número de 3 algarismos "))

if (num >= 100 and num <=999):
    div100 = num//100
    print(div100)

else:
    print("O número informado não é um número de 3 algarismos")

