# 1. Um ângulo é chamado agudo se é menor que 90 graus, obtuso se é maior do que 90 graus ou reto caso seja
# exatamente 90 graus. Implemente um programa que receba um ângulo (número real) como entrada
# e responda qual é o tipo de ângulo.

graus = float(input("Digite um numero do angulo: "))

if graus < 90:
    print("O angulo eh agudo")
elif graus == 90:
    print("O angulo eh reto")
else:
    print("O angulo eh obtuso")