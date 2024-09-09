#IMC 
print("Programa oara Cálculo de IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float (input("Digite a sua altura (em metros): "))
imc = peso/ (altura ** 2)

print(f"Seu IMC é {imc:.2f}.")
print ("Classificação do IMC: ")
if imc < 18.5:
    print("Abaixo do peso normal.")
elif 18.5 <= imc < 25:
    print ("Peso normal.")
elif 25 <= imc < 30:
    print("Sobrepeso.")
elif 30 <= imc < 35:
    print("Obesidade grau I.")
elif 35 <= imc < 40: 
    print("Obesidade grau II.")
else:
    print ("Obesidade grau III")