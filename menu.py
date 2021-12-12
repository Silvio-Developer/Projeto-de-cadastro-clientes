from linhas import linha
from subMenu import sub_menu
import os

def menu_principal():

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
                sub_menu()
            elif op_user == 3:
                print('\tEncerrando sistema!')
                os.system('pause')
                break
        else:
            print('\tOpção invalida!')
            os.system('pause')

