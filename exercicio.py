def tem_digitos_adjacentes_iguais(numero):
    numero_str = str(numero) 
    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i + 1]:
            return True
    return False
n= int(input("quantos numeros deseja verificar?"))

for _ in range(n):
    num = int(input("digite um numero inteiro:"))
    if tem_digitos_adjacentes_iguais (num):
        print(f"O número {num} tem digitos adjacentes iguais.")
    else:
        print(f"O número {num} não tem adjacentes iguais.")