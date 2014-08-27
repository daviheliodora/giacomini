#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
['Davi Roberto de Souza', '2014-07-16', '10:58:42.0', 'Presente', '7241/6297']
'''

#info_arq = []

def data_atual():
    from datetime import datetime
    today = datetime.now()
    data = str(today).split(' ')[0]
    return data

def gerar_arquivo(nome):

    try:
        arq = open('_'.join(nome.split(' '))+'.txt', 'r')
        arq.close()
        arq1 = open('_'.join(nome.split(' '))+'_total_horas.txt', 'r')
        arq1.close()
    except IOError:
        arq = open('_'.join(nome.split(' '))+'.txt', 'w')
        arq.close()
        arq1 = open('_'.join(nome.split(' '))+'_total_horas.txt', 'w')
        arq1.close()

        

def gravar(info):
    info_arq = pegar_ult_reg(info)
    lista = []
    lista_gravar = []

    if info_arq[-1].split('/')[0] != data_atual():
        info_arq.append(info)
        lista = info_arq
    else:
        lista = info_arq[:-1]
        lista.append(info)

    nome = info.split('/')[1]

    arq = open('_'.join(nome.split(' '))+'.txt', 'w')
    arq.write('\n'.join(lista))
    arq.close()

    info_arq = []

def pegar_ult_reg(info):
    info_arq = []

    nome = info.split('/')[1]
    arq = open('_'.join(nome.split(' '))+'.txt', 'r')

    for linha in arq.read().split('\n'):
        info_arq.append(linha)
    arq.close()
    return info_arq

def gerar_arq_tot_hr_trab(info):

    info_arq = []
    lista = []
    nome = info[1]
    
    arq_hr = open('_'.join(nome.split(' '))+'_total_horas.txt', 'r')
    for linha in arq_hr.read().split('\n'):
        info_arq.append(linha)
    arq_hr.close()

    ult_reg = info_arq[-1:]
    data_ult_reg = ''.join(ult_reg).split('/')[0]
    if info[0] == data_ult_reg:
        lista = info_arq[:-1]
    else:
        lista = info_arq
    lista.append('/'.join(info))
    
    arquivo = open('_'.join(nome.split(' '))+'_total_horas.txt', 'w')
    arquivo.write('\n'.join(lista))
    arquivo.close()
    
