class Cafeteira:
  def __init__(self, marca, tipo, tamanho, cor):
    self.marca = marca
    self.tipo = tipo
    self.tamanho = tamanho
    self.cor = cor

class Cachorro:
  def __init__(self, raça, idade, nome, cor):
    self.raça = raça
    self.idade = idade
    self.nome = nome
    self.cor = cor
    
rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')
print(rex.idade == '2')

class Lista:
  def append(self, elemento):
    return "Oops! Este objeto não é uma lista"
    
lista = []

a = Lista()
b = a.append(7)
print(b)

lista.append(b)
print(lista)