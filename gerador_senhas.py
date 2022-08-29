import random

print("Gerador de Senhas\n");

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*^().,?0123456789";

numero= int(input("Digite quantidade de senhas que deseja gerar: "));

tamanho = int(8);

print("Esses são os exemplos:")

for pwd in range(numero):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(chars)
    print(senhas);
