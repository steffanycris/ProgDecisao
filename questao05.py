'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

n1 = float(input("Informe a primeira nota "))
n2 = float(input("Informe a segunda nota "))
n3 = float(input("Informe a terceira nota "))
n4 = float(input("Informe a quarta nota "))

media = (n1+n2+n3+n4)/4

situacao = ("REPROVADO","APROVADO")[ media>=5 ]

print(situacao)
print("Sua média foi igual à: ",media)