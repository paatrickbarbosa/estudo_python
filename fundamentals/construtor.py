class Pessoa:
    nome = None;
    idade = None;

    def _ini_ (self,n,i):
        self.nome = n;
        self.idade = i;

    def imprimirNome(self):
        print(self.nome);
        
    def imprimirIdade(self):
        print(self.idade);

    def colocarIdade(self,num):
        self.idade = num

        
    def colocarNome(self,nom):
        self.nome = nom;

emerson = Pessoa("Emerson",30)

emerson.imprimirNome()
emerson.imprimirIdade()        
