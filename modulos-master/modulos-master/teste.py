import moeda

print('#### PROGRAMA VALORES ####')
while True:
    try:
        p = float(input('\nDigite o preço: R$'))
        t = int(input('Digite a taxa de aumento: '))
        d = int(input('Digite a taxa de desconto: '))

    except (ValueError, TypeError):
        print('Erro no tipo de dado digitado. Digite somente numero inteiro ou real!')

    except KeyboardInterrupt:
        print('O usuario não informou os dados')
    else:
        moeda.resumo(p, t, d)
        res = str(input('Deseja sair do programa?[S/N] '))
        if res in 'Ss':
            break
        else:
            continue
print("Obrigado por sua visita! ^^")





