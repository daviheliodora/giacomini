#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

def calc_tempo(hora):

    h1,m1 = hora.split(':')

    return int(h1)*60 +int(m1)

def hora_atual():
    ''' Código para pegar data e hora do sistema '''
    from datetime import datetime
    today = datetime.now()
    day = today.day
    month = today.month
    year = today.year

    return str(today.hour)+":"+str(today.minute).zfill(2)

def data():
    today = datetime.now()
    return str(today.date())

def data_atual():
    from datetime import datetime
    today = datetime.now()
    data = str(today).split(' ')[0]
    return data

def tot(in1, out1, in2, out2):
    tot1 = dif_horas(in1, out1)
    tot2 = dif_horas(in2, out2)
    tot = somar_hr(tot1, tot2)
    return tot

def dif_horas(hora1, hora2):
    # retorna hora2 - hora1

    h1,m1 = hora1.split(':')
    h2,m2 = hora2.split(':')

    aux = str(timedelta(hours=int(h2), minutes=int(m2)) - timedelta(hours=int(h1), minutes=int(m1)))

    hora = ':'.join(aux.split(':')[:2])

    return hora

def somar_hr(hora1, hora2):
    # retorna hora2 + hora1

    h1,m1 = hora1.split(':')
    h2,m2 = hora2.split(':')

    aux = str(timedelta(hours=int(h2), minutes=int(m2)) + timedelta(hours=int(h1), minutes=int(m1)))

    hora = ':'.join(aux.split(':')[:2])

    return hora

def info(nome):

    dados = ''

    arq = open('_'.join(nome.split(' '))+'.txt', 'r')

    for linha in arq.read().split('\n'):
        dados = linha

    arq.close()

    return dados

def gerar_total_horas_trab(pessoa):

    hr_total = ''

    dados = info(pessoa).split('/')

    tam = len(dados)

    if tam == 3:
        hora = dados[2]
        hr_total = dif_horas(hora, hora_atual())

    if tam == 4:
        hora1 = dados[2]
        hora2 = dados[3]
        hr_total = dif_horas(hora1, hora2)

    if tam == 5:
        hora1 = dados[2]
        hora2 = dados[3]
        hr_parc = dif_horas(hora1, hora2)
        
        hora3 = dados[4]
        hr_parc2 = dif_horas(hora3, hora_atual())
        
        hr_total = somar_hr(hr_parc, hr_parc2)

    if tam == 6:
        hora1 = dados[2]
        hora2 = dados[3]
        hr_parc = dif_horas(hora1, hora2)
        
        hora3 = dados[4]
        hora4 = dados[5]
        hr_parc2 = dif_horas(hora3, hora4)
        
        hr_total = somar_hr(hr_parc, hr_parc2)


    return hr_total

