#calculadora de fatoriual: criar um programa que calcule o fatorial de
#um número fornecido pelo usuárioi usando um loop while.

numero = (int("Digite um número:"))
fatorial = 1
contador = 1

while (contador <= numero):
    fatorial*= contador # fatorial = fatorial * contador
    contador += 1 # contador = contador + 1

    print(f"o fatorial de {numero} é {fatorial}")