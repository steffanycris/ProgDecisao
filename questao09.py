'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Informe um número "))

#resposta por meio de operador ternario
resposta = f"{num} é positivo" if num > 0 else f"{num} é negativo" if num < 0 else f"{num} é nulo"

print(resposta)


'''

if ( num > 0 ):

    print(f"{num} é positivo")

elif (num < 0):

    print(f"{num} é negativo")

else:

    print(f"{num} é nulo")
'''