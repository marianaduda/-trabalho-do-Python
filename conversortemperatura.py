def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def menu():
    print("Selecione a conversão de temperatura:")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")
    escolha = int(input("Digite sua escolha (1-6): "))
    temperatura = float(input("Digite a temperatura: "))

    if escolha == 1:
        print(f"{temperatura} Celsius é igual a {celsius_para_fahrenheit(temperatura)} Fahrenheit.")
    elif escolha == 2:
        print(f"{temperatura} Celsius é igual a {celsius_para_kelvin(temperatura)} Kelvin.")
    elif escolha == 3:
        print(f"{temperatura} Fahrenheit é igual a {fahrenheit_para_celsius(temperatura)} Celsius.")
    elif escolha == 4:
        print(f"{temperatura} Fahrenheit é igual a {fahrenheit_para_kelvin(temperatura)} Kelvin.")
    elif escolha == 5:
        print(f"{temperatura} Kelvin é igual a {kelvin_para_celsius(temperatura)} Celsius.")
    elif escolha == 6:
        print(f"{temperatura} Kelvin é igual a {kelvin_para_fahrenheit(temperatura)} Fahrenheit.")
    else:
        print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    while True:
        menu()
        continuar = input("Você quer converter outra temperatura? (s/n): ")
        if continuar.lower() != 's':
            break
