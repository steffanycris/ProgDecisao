# Crie um programa que pergunte um número ao usuário
#Em seguida o programa deve informar se o número inserido esta abaixo de 100, entre 100 e 200 ou acima de 200.
'''
 print(type(num))  - para mostrar o tipo de variável
 '''


num = int(input("Digite um número: "))

if ( num < 100 ):
    print(f"{num} é menor que 100: ")
else:
    # aqui está a partir de 100
    if(num >= 100 and num <= 200):
       print(f"{num} está entre 100 e 200")
    else:
       print(f"{num} está acima de 200")