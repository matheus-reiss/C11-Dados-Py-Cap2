#1.
nome = input("Digite seu nome completo: ").strip()

print("Nome em Maiúsculo: ", nome.upper())
print("Nome em Minúsculo: ", nome.lower())
print("Total de letras: ", len(nome.replace(" ", "")))

# Fazendo troca do ultimo nome para do Inatel
partes = nome.split()
if len(partes) > 1:
    partes[-1] = "do Inatel"
else: 
    partes.append("do Inatel")
novoNome = ' '.join(partes)
print("Nome com ultimo sobrenome trocado: ",novoNome)


#2.

print("\nTabuada")
inicio = None
fim = None 
numero = None
entradaValida = False

while not entradaValida:
    try:
        inicio = int(input("Digite o ínicio para o intervalo: "))
        fim = int(input("Digite o fim do intervalo: "))
        if inicio > fim:
            print("O início deve ser menor ou igual ao fím.")
        else:
            numero = int(input("Digite o número para ver a tabuada: "))
            entradaValida = True
    except ValueError:
        print("Digite apenas numeros inteiros")

print(f"\n Tabuada do {numero} de {inicio} a {fim}: ")
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")
        


#3.
sexo = input("Digite o sexo (M para homem / F para mulher): ").strip().upper()

while sexo !='M' and sexo !='F':
    print("Sexo inválido. Por favor, digite M ou F.")
    sexo = input("Digite o sexo (M para homem / F para mulher): ").strip().upper() 

if sexo == 'M':
    print("Você é homem.")
else:
    print("Você é mulher.")