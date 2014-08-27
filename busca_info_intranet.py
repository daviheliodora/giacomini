#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time



#registro = []

def pega_info_intranet():

    arq = open("arq_intranet.txt", 'w')
    arq.write('')
    arq.close()

    try:
        response = requests.get("http://intranet.lit.inpe.br/node/9")
        arq = open("arq_intranet.txt", 'w')
        arq.write(response.content)
        arq.close()
    except ConnectionError as erro:
        print 'Erro ao conectar a intranet, nova tentativa em 1 minuto...'
        time.sleep(60)
        pega_info_intranet()

    
        
def pegar_info(info):
    a=''
    atual = ''

    #i = []
    
    arquivo = open("arq_intranet.txt", 'r')
    
    for linha in arquivo.readlines():
        #verifica se eh a linha com as informacoes certas
        if '<form><input type="button" value="Imprimir lista"' in linha:
            info.append(linha)

        # pega informacao da atualizacao da pagina
        if 'realizada em &nbsp;<font color="red">' in linha:
            atual=str(linha.split('realizada em &nbsp;<font color="red">')[-1].split('<')[0].split(' ')[1])
    arquivo.close()

    #[ info.pop() for x in xrange(len(info)) ]
    #info = i

    
        

def atualizacao_sistema():

    atual = ''
    arquivo = open("arq_intranet.txt", 'r')
    
    for linha in arquivo.readlines():
        # pega informacao da atualizacao da pagina
        if 'realizada em &nbsp;<font color="red">' in linha:
            atual=str(linha.split('realizada em &nbsp;<font color="red">')[-1].split('<')[0].split(' ')[1])
        

    arquivo.close()

    return atual

    
def pega_info_usuarios(tempo):

    info = []
    reg = []

    if tempo > 30:
        pega_info_intranet()# atualiza arquivo txt com a intranet
        

    pegar_info(info) # gera lista []  com informacoes dos funcionarios

    user = ''
    if 'width:35px"><a' in info[0]:
        user = info[0].split('width:35px"><a ')

    nome = ''
    data_reg = ''
    hora_reg = ''
    status = ''
    ramal = ''
    
    num = len(user)

    for i in range(1,num):

        #separa as informacaos
        alt      = user[i].split('alt=')

        stus   = alt[2].split("' ")[0]
        status   = stus[1:].split(':')[0]

        title    = user[i].split('title=')

        registro = title[2].split("/></div><div")[0].split("'")[1]
        data_reg = registro.split(': ')[1].split(' ')[0]
        hora_reg = registro.split(': ')[1].split(' ')[1]

        name     = user[i].split('color:#000000;"><a href=')
        nome     = name[1].split("'>")[1].split('</a></span>')[0]

        r        = user[i].split('Ramal')
        ramal    = r[1].split('</b><b')[0][2:]

        reg.append([nome, data_reg, hora_reg, status, ramal])
    

    return reg
            
def exibir_pessoas(registro):

    for func in registro:
        print 'Nome:     ',func[0]
        print 'data:     ',func[1]
        print 'hora:     ',func[2]
        print 'Status:   ',func[3]
        print 'Ramal:    ',func[4]
        print '============================'
    

