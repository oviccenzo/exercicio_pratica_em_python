# 17. Um americano em visita ao Brasil tinha muita dificuldade na hora de escolher entre
# “bermudas” ou “calças”, pois ele não entendia nossa medida de temperatura (celsius).
# Escreva um programa que, após a entrada da temperatura em Celsius (C), escreva a
# temperatura em Fahrenheits (F) e também o que vestir. Dado que:
# F = (9C + 160)/5;
# Ele irá vestir:
# calças se F < 65,
# bermudas em caso contrário.

c = float(input('Digite a temperatura em Celsius para converter para Fahrenheit: '))

f = (9 * c + 160) / 5

print(f"A temperatura farenheit eh: {f}")

if f < 65:
    print('Ele ira vestir: bermudas')
else:
    print('Ele ira vestir: calça')

