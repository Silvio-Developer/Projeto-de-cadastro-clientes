from linhas import linha
import os
def exibir_dados():
    os.system('cls')
    print('\n\n')
    linha('*', 100)
    print(f'\t{"Clientes Cadastrados":^100}')
    linha('*', 100)
    print()
    linha('=', 100)
    print(f'\t{"CPF":^13} | {"Nome":<30} | {"Telefone":^12} | {"Email"}')
    print('\t--------------+--------------------------------+--------------+-------------------------------------')
    with open('clientes\cadastros.txt', 'r') as dados_file:
        for l in dados_file:
            dados = l.split(';')
            print(f'\t{dados[0]:>13} | {dados[1]:<30} | {dados[2]:<12} | {dados[3]}', end='')
            print('\t--------------+--------------------------------+--------------+-------------------------------------')
    print('\t')
    os.system('pause')
