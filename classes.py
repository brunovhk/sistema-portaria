from datetime import datetime


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


class Autorizado:
    def cadastraAutorizado(autorizados):
        print('Preencha o formulário de cadastro de visitante:')
        nome_visitante = str.lower(input('Nome do visitante: '))
        numero_casa = input('Número da casa: ')
        nome_morador = input('Entrada autorizada por: ')
        print(f'\nNome do visitante: {nome_visitante}')
        print(f'Número da casa: {numero_casa}')
        print(f'Entrada autorizada por: {nome_morador}\n')
        autorizado = nome_visitante, numero_casa, nome_morador
        autorizados.append(autorizado)
        print('Cadastro de visitante autorizado efetuado com sucesso.\n')

    def listarAutorizados(autorizados):
        for autorizado in autorizados:
            nome_visitante, numero_casa, nome_morador = autorizado
            print(f'Nome do visitante: {nome_visitante}, Numero da casa: {numero_casa}, Autorizado por: {nome_morador}')

    def verificarAutorizado(autorizados):
        nome_desejado = str.lower(input('Nome do visitante: '))
        for autorizado in autorizados:
            nome_visitante, numero_casa, nome_morador = autorizado
        if nome_desejado == nome_visitante:
            print('Visitante:')
            print(
                f'Nome: {nome_visitante}, '
                f'Número da casa: {numero_casa}, '
                f'Entrada autorizada por: {nome_morador}\n')
            return True
        else:
            print('Nome de visitante não encontrado.')


class Visitante:
    def cadastrarVisitantes(visitantes):
        print('#' * 30)
        print('Preencha o formulário de entrada do visitante:')
        print('#' * 30)
        rg = input('RG: ')
        nome_visitante = str.lower(input('Nome: '))
        casa_destino = input('Casa de destino: ')
        nome_morador = input('Pessoa que autorizou: ')
        hora = datetime.now()
        entrada = hora.strftime('%d/%m/%Y, %H:%M')
        acompanhantes = input('Nome dos acompanhantes: ')
        print('-' * 30)
        print(f'Número da casa: {nome_visitante}')
        print(f'RG: {rg}')
        print(f'Autorizado por: {nome_morador}')
        print(f'Horario de entrada: {entrada}')
        print(f'Acompanhantes: {acompanhantes}')
        visitante = rg, nome_visitante, casa_destino, nome_morador, entrada, acompanhantes
        visitantes.append(visitante)
        print('Cadastro de entrada efetuado com sucesso.\n')
