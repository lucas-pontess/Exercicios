'''Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo. '''

print("Dados da primeira pessoa:")
nome1 = str(input("Nome: "))
idade1 = int(input("Idade:"))
print("Dados da segunda pessoa:")
nome2 = str(input("Nome: "))
idade2 = int(input("Idade:"))

media = (idade1 + idade2) / 2

print(f"A idade media de {nome1} e {nome2} e de {media:.1f} anos")
