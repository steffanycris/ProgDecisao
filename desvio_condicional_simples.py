
'''
Crie um programa que pergunte dois números ao usuário.
Em seguida o programa deverá somar os dois números e apresentar o
resultado se o valor for maior que 10
'''

n1 = int(input("Informe um número:"))
n2 = int(input("Informe outro número:"))

soma = n1+n2

# o parenteses no if é opicional .Tipo: "  if soma>10 :  "
if (soma > 10 ):
    print(f"A soma dos números é maior que 10  sendo ela {soma}") # esta dentro do código "if" pois está com um tab de diferença
print("vish") # ta fora do código de "if" pela identação não estar compatível.