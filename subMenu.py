from linhas import linha
from salvar import salvar_cadastro
from exibir import exibir_dados
import os
def sub_menu():
    while True:
        op_sub = ['Salvar', 'Excluir', 'Exibir Clientes', 'Voltar']
        os.system('cls')
        linha()
        for index, op in enumerate(op_sub):
            print(f'\t\t[{index + 1}] - {op}')
        linha('-')
        op_user = input('\tDigite opção: ')
        if op_user.isdigit():
            op_user = int(op_user)
            if op_user == 1:
                salvar_cadastro()
            elif op_user == 2:
                print('Excluir dados')
            elif op_user == 3:
                exibir_dados()
            elif op_user == 4:
                break
