class Pessoa:

    #def (self, nome = idade = 0, peso=0.0, altura=0.0):
      #  self.nome = nome
      #  self.idade = idade
    #self.peso = peso
   # self.altura = altur

    def envelhecer (self):
        self.idade += 1
        if self.idade < 21:
            self.crescer (0.5)

    def engordar (self, valor):
        self.peso += valor

    def emagrecer (self, valor):
        self.peso -= valor

    def crescer (self, valor):
        self.altura += valor

if __name__ == '__main__':
    pessoa = Pessoa (nome="yugu", idade="654", peso="546", altura="45546")
    print ("Antes: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso}, Altura: {pessoa.altura}")
    pessoa.envelhecer(1)
    pessoa.engordar(5)
    pessoa.emagrecer(6)
    pessoa.crescer(1.70)
    print ("Depois: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso}, Altura: {pessoa.altura}")