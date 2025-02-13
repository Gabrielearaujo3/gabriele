class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
  def apresentar(self):
    print(f"Nome: {self.nome}")
    print(f"Idade: {self.idade} anos")
    print(f"Peso: {self.peso} kg")
    print(f"Altura: {self.altura} mtros")
   
pessoa1 = Pessoa("Emanuela", 18, 55, 1.66)
pessoa1.apresentar