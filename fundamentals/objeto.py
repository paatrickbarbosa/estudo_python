class Pessoa:
    nome = None;
    idade = 20;

    def imprimirNome(self):
        print(self.nome);
        
    def imprimirIdade(self):
        print(self.idade);

    def colocarIdade(self,num):
        self.idade = num

        
    def colocarNome(self,nom):
        self.nome = nom;

emerson = Pessoa()
emerson.colocarIdade(30)
emerson.colocarNome("Emerson Ferrovia")

emerson.imprimirNome()
emerson.imprimirIdade()        
