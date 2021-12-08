import numpy as np
import matplotlib.pyplot as plt

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos')

    def ano_nascimento(self, ano_atual):
        ano = ano_atual - self.idade
        print(f'Vc nasceu no ano de {ano}')
  
objects = Pessoa('Arthur', 22)
print('Done!')
