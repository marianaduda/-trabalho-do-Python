#Algoritmo de média: criar um algoritmo que leia 4 notas e  apresente a media ao final


print("Olá! Vamos ver qual será sua média.")

nota1 = float(input("Digite a primeira nota:" ))
nota2 =float (input("Digite a segunda nota:" ))
nota3 =float (input("Digite a terceira nota:" ))
nota4 =float (input("Digite a quarta nota:" ))
media = (nota1 + nota2 + nota3 + nota4 ) / 4
print("A média final obtida ", media)

if(media >= 80):
    print("Aluno aprovado!!!")
else:
    print("Aluno reprovado!!!")
        