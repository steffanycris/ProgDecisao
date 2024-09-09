"""
Crie um programa que pergunte a idade de uma pessoa.
Em seguida o programa deve informar se a pessoa é menor de idade
ou se é maior de idade
"""

idade = int(input("Informe sua idade por gentileza :"))

if (idade < 18) :
         print("Você ainda é menor de idade.")
else :
    if (idade > 18) :
        print("Você é maior de idade .")