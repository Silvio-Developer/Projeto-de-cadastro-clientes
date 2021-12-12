from linhas import linha
import os
while True:
    op_menu = ['Cadastros', 'Sobre', 'Sair']
    os.system('cls')
    linha()
    for index, op in enumerate(op_menu):
        print(f'\t\t[{index + 1}] - {op.upper()}')
    linha('-')
    op_user = input('\tDigite opção: ')
    if op_user.isdigit():
        op_user = int(op_user)
        if op_user == 1:
            print('Cadastro')
        elif op_user == 3:
            break
    else:
        print('\tOpção invalida!', end=' ')
        os.system('pause')

