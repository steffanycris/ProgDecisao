"""
1) Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
"""

num = int(input("Informe um número:"))


#lógica do op ternário1: var = (se for falso, se for verdadeiro)[teste condicional]
resposta = (f"o número é {num}" ,f"A metade é {num/2}")[20 < num]
print(resposta)


#var = resultado_verdadeiro if teste_condicional else resultado_falso
resposta = f"A metade é {num/2}" if num > 20 else f"O número é {num}"
print(resposta)