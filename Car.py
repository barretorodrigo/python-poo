class Carro():
    """ Criando o modelo de carro para nosso objetos """
    def __init__(self, marca, ano, modelo):
      """ Método construtor para iniciar as propriedades """
      self.marca = marca
      self.ano = ano
      self.modelo = modelo

    def acelerar(self):
      """ Método para simular a ação de acelerar do carro """
      print('Vruummm')

    def escreve_descricao(self):
        print(self.marca + ' - ' + self.modelo + ' - ' + str(self.ano))

fusca = Carro('VW', 1970, 'Fusca')

fusca.escreve_descricao()