# 25. O Peso normal de uma criança pode ser calculado através da fórmula:
# PesoNormal = idade - 6 / 4.4 + 2.3 * (idade - 6) + 22
#  Escreva um programa que leia a idade e o peso de uma criança e, se for o caso, imprima
# uma dessas mensagens de acordo com a quantidade de quilos acima do peso com que a
# criança esteja:
# Quantidade de quilos acima do peso
# De 2 a 5
# Acima de 5 ate 10
# Acima de 10
# Mensagem
# “Parar de tomar refrigerante.”
# “Parar de comer doces.”
# “Parar de tomar refrigerante e de comer doces.”

idade = int(input('Digite sua idade: '))
peso_ideal = float(input('Digite seu peso atual: '))

PesoNormal = (idade - 6) / 4.4 + 2.3 * (idade - 6) + 22

acima_do_peso = peso_ideal - PesoNormal

if 2 <= acima_do_peso <= 5:
    print("Parar de tomar refrigerante")
elif 5 < acima_do_peso <= 10:
    print("Parar de comer doces")
elif acima_do_peso > 10:
    print("Parar de tomar refrigerante e de comer doces")

print(f'O seu peso ideal eh: {PesoNormal} kg')