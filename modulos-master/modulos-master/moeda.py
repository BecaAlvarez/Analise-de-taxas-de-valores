def aumentar(preco = 0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res= preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco/2
    return res if not formato else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def taxa(preco = 0, taxa = '%'):
    return f'{preco:.0f}{taxa}'.replace('.', ',')


def resumo(p= 0, t = 10, d = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(20))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(p)}')
    print(f'O dobro do preço:\t{dobro(p, True)}')
    print(f'A metade do preço:\t{metade(p, True)}')
    print(f'Adicional de {taxa(t)}:\t{aumentar(p, t, True)}')
    print(f'Desconto de {taxa(d)}:\t{diminuir(p, d, True)}')
    print('-' * 30)