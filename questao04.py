'''
4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Informe um número"))

resto4 = (num%4)
resto5 = (num%5)

print("O número é divisível por 4 e por 5! " if (resto4 == 0) and (resto5 == 0) else "O número não é divisível por 4 e 5")