import os
import json


def salvar_cadastro():
    while True:
        os.system('cls')
        print('\n\tCadastro de Clientes\n\n')
        cpf = input(f'{"CPF: ":>20}')
        nome = input(f'{"Nome completo: ":>20}')
        telefone = input(f'{"Telefone: ":>20}')
        email = input(f'{"E-mail: ":>20}')
        if len(nome) != 0 and len(telefone) != 0 and telefone.isdigit() and len(email) != 0 and len(cpf) != 0:
            arq = open('clientes\cadastros.txt', 'a')
            # dados = f"'cpf': '{cpf}', 'nome': '{nome}', 'telefone': '{telefone}', 'email': '{email}'\n"
            dados = f'{cpf};{nome};{telefone};{email}\n'
            arq.write(dados)
            print('\n\tDados salvos com sucesso!!!')
        else:
            print('\n\tDados invalidos! Verifique os dados informados')
            os.system('pause')
        op_user = input('\n\tDeseja continuar? [Enter=Sim/n=não]: ')
        if op_user.upper() == 'N':
            break
