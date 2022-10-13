entrada = input("Digite um numero: ");
num = int(entrada);


if not 0 < num < 110:
    print("O numero digitado foi invalido");

if num % 2 == 0:
    print("O numero digitado foi par");

if num % 2 != 0:
    print("O numero digitado foi impar")
    
