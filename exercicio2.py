calc = float(input("Digite qual operação deseja realizar: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))

if calc == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A soma dos números é: {num1 + num2}")
elif calc == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A subtração dos números é: {num1 - num2}")
elif calc == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A multiplicação dos números é: {num1 * num2}")
elif calc == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A divisão dos números é: {num1 / num2}")
else:
    print("Operação inválida ou inexistente")