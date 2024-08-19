n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Escolha a operação: 1-Soma, 2-Subtração, 3-Multiplicação e 4-Divisão: "))
    
if n3 == 1:
    resultado = n1 + n2
elif n3 == 2:
    resultado = n1 - n2
elif n3 == 3:
    resultado = n1 * n2
elif n3 == 4:
    resultado = n1 / n2
else:
    resultado = 0

print("Resultado:", resultado)