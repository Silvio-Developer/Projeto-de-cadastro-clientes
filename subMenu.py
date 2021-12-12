from linhas import linha
import os
def sub_menu():
    while True:
        op_sub = ['Salvar', 'Excluir', 'Lista', 'Voltar']
        os.system('cls')
        linha()
        for index, op in enumerate(op_sub):
            print(f'\t\t[{index + 1}] - {op}')
        linha('-')
        op_user = input('\tDigite opção: ')
        if op_user.isdigit():
            op_user = int(op_user)
            if op_user == 1:
                print('Salvar dados')
            elif op_user == 2:
                print('Excluir dados')
            elif op_user == 3:
                print('Listar dados')
            elif op_user == 4:
                print('Voltando ao menu prncipal')
                os.system('pause')
                break