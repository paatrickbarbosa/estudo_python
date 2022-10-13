try:
    arquivo = 'notas.txt';
    arq = open(arquivo, 'r');
    texto = arq.read();
    print(texto);
  
except:
    print("Arquivo " + arquivo + " nao encontrado");


