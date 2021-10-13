import json
from validate_docbr import CPF

novo_cpf = input('DIGITE SEU CPF:  ')
cpf = CPF()
lista_cpf = []

with open('cpf_validor/database/database.json', 'r') as load_json:
    dados = json.load(load_json)

lista_cpf = dados

def validador(novo_cpf):
    if cpf.validate(novo_cpf):
        print(f'O CPF {novo_cpf} É VÁLIDO!')
        lista_cpf.append(novo_cpf)
    else:
        print(f'O CPF {novo_cpf} É INVÁLIDO!')

validador(novo_cpf)

with open('cpf_validor/database/database.json', 'w') as write_json:
    json.dump(lista_cpf, write_json)
