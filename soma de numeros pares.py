#Soma de números pares: Desenvolver um programa que solicita ao 
#Usuario de um número e, em seguida, calcula a soma de todos os 
# números pares até esse número, utilizando um loop while 

numero = int(input("Digite um número: "))

#Inicializando variaveis 

Soma_pares = 0
contador = 2 # o primeiro número par 

#calculando a soma dos números pares usando o loop while 
while contador <= numero:
    #print (f"{soma_pares} + {contador} = {soma_pares + contador}"")
    Soma_pares += contador # soma_pares = soma_pares + contador
    contador += 2 # avançando para o próximo número par 

    # Exibindo o resultado 
    print(f"A soma dos números pares até {numero} é:  {Soma_pares}")

    ################
    # utilizando if 
    # solicitar ao usuario o número 
    numero = int(input("Digite um número: "))

    #inicializando variáveis 
    soma_pares = 0
    contador = 1 # iniciando em 1, o primeiro número impar 
    
    # calculando a soma dos números pares usando o loop while com desvio 
    # Condicional if 
    while contador <= numero: 
        if contador % 2 == 0: # verifica se o número é par 
            soma_pares += contador 
        contador += 1 # avança para o próximo número 

    # Exibindo o resultado 
    print(f"A soma dos números pares até {numero} é:  {soma_pares}")