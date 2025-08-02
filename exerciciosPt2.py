#4.
distancia = float(input("Digite a distancia da viagem em km: "))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f"O preço da passagem é: R${preco:.2f}")

#5. 
numero = int(input("Digite um número entre 1000 e 9999: "))
while numero < 1000 or numero > 9999:
    print("Número fora do intervalo. Tente novamente.")
    numero = int(input("Digite um número entre 1000 e 9999: "))

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print("Milhar:", milhar)
print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)

#6.
import math

entradaValida = False

while not entradaValida:
    entrada = input("Digite um número decimal: ").strip()
    entrada = entrada.replace(",",".")

    try:
        numero = float(entrada)

        if numero == int(numero):
            print("Você digitou um número inteiro. Por favor digite um número decimal.")
        else:
            entradaValida = True
    except ValueError:
        print("Entrada inválida. Digite um número como 2.5 ou 3,14.")

raiz = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parteInteira = int(numero)

print(f"\nRaiz quadrada: {raiz:.2f}")
print(f"Teto (ceil): {teto}")
print(f"Chão (floor): {chao}")
print(f"Parte inteira: {parteInteira}")
