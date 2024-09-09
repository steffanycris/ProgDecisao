'''
6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

n1 = int(input("Informe o primeiro valor "))
n2 = int(input("Informe o segundo valor "))

resposta = (n1-n2) if (n1>n2) else (n2-n1)

print("A diferença desses números é: ")
print(resposta)

