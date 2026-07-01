# 4. Faça um programa que leia 2 números positivos e imprima o menor deles.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite dois numero: '))

print(num1)
print(num2)

if num1 < num2:
    print(f"O menor número eh: {num1}")
else:
    print(f"O menor número eh {num2}")