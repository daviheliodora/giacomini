#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atualizar_arquivo import gravar
from contabilizar_horas_trab import data_atual



def pegar_ult_reg(nome):

    inf = ''

    arq = open('_'.join(nome.split(' '))+'.txt', 'r')

    for linha in arq.read().split('\n'):
        if linha != '':
            inf = linha
    arq.close()

    return inf

def verificar_situacao(nome):

    inf = pegar_ult_reg(nome)

    if inf.split('/')[0] != data_atual():
        return 0

    return len(inf.split('/'))

def inicio_expediente(func):

    nome = func[0]
    data = func[1]
    h = func[2]
    aux = h.split(':')[:2]
    hora = ':'.join(aux)

    return  '/'.join([data, nome, hora])
    

def tratar_informacao(func):
    '''
    ['Davi Roberto de Souza', '2014-07-16', '10:58:42.0', 'Presente', '7241/6297']
    '''

    nova_linha = ''
    valor = verificar_situacao(func[0]) # verifica se data atual é igual ultimo valor regisdtrado no txt

    if valor == 0 and func[3] == 'Presente': # inicio expediente        
        nova_linha = inicio_expediente(func)
        
    if valor == 3 and func[3] == 'Ausente': #saida almoco
        linha = pegar_ult_reg(func[0])
        nova_linha = linha+'/'+func[2][:5]
        
    if valor == 4 and func[3] == 'Presente': #volta almoco
        linha = pegar_ult_reg(func[0])
        nova_linha = linha+'/'+func[2][:5]
        
    if valor == 5 and func[3] == 'Ausente': #fim expediente
        linha = pegar_ult_reg(func[0])
        nova_linha = linha+'/'+func[2][:5]

    if nova_linha != '':
        gravar(nova_linha) # nova linha no formato -> '2014-07-17/Davi Roberto de Souza/8:00/12:00/13:30'

#tratar_informacao(['Davi Roberto de Souza', '2014-08-07', '17:00:42.0', 'Ausente', '7241/6297'])
