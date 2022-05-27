from classes import *

autorizados = []
visitantes = []
op1 = 'Cadastrar visitante'
op2 = 'Cadastrar entrada de visitante'
op3 = 'Verificar acesso de visitante'
op4 = 'Ver todas as entradas autorizadas'
op5 = 'Sair do sistema'
while True:
    resposta = menu([op1, op2, op3, op4, op5])
    if resposta == 1:
        Autorizado.cadastraAutorizado(autorizados)
    elif resposta == 2:
        Visitante.cadastrarVisitantes(visitantes)
    elif resposta == 3:
        if Autorizado.verificarAutorizado(autorizados):
            Visitante.cadastrarVisitantes(visitantes)
    elif resposta == 4:
        Autorizado.listarAutorizados(autorizados)
    elif resposta == 5:
        print('Sistema finalizado.')
        break
    else:
        print('Erro! Digite uma opção válida!')
