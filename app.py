from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('João', 9)
restaurante_praca.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('Pedro', 2)

bebida_suco = Bebida('Suco de Laranja', 5.0, '400ml')
prato_bife = Prato('Bife Acebolado', 25.0, 'Bife com cebolas caramelizadas e arroz branco')

restaurante_praca.adicionar_bebida_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_cardapio(prato_bife)


def main():
    Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(prato_bife)

if __name__ == '__main__':
    main()