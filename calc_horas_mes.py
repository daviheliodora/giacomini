#!/usr/bin/env python
# -*- coding: utf-8 -*-


def soma_tot_mes(nome):
    dados = []
    horas = []
    ler_arq_registro_tot_horas(nome, dados)

    for item in dados:

        data, nome, tot_dia = item.split('/')
        if tot_dia != '':
            horas.append(converte_minutos(tot_dia))
    total = somar_horas(horas)

    return str(total)[:5]+'/'+str((21*8))

def somar_horas(horas):
    total = 0
    while horas:
        tempo = horas.pop()
        total = total+ tempo

    total = conv_hora(total)

    return total

def conv_hora(total):
    return total/60
    
def converte_minutos(hora):
    h,m = hora.split(':')

    return float(m)+(float(h)*60)

def tot_mes():
    return ''




def ler_arq_registro_tot_horas(nome, dados):

    nome = '_'.join(nome.split(' '))
    arq = open(nome+'_total_horas.txt', 'r')

    for linha in arq.read().split('\n'):
        if linha != '':
            dados.append(linha)

    arq.close()

