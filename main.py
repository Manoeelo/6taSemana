# 1 - imports - bibliotecas
import pytest
# 2 - class - classes

# 3 - definitions - definições = métodos e funções
def print_hi(name):
    print(f'Hi, {name}')

def calculo_fosforos(num,qtd):
    return num * qtd

def teste_calculo():
    assert calculo_fosforos(40,5) == 200


if __name__ == '__main__':
    print_hi('PyCharm')

    resultado = calculo_fosforos(40,5)
    print(f'Você comprou {resultado} palitos')
