#!/usr/bin/env python
# -*- coding: utf-8 -*-

from busca_info_intranet import pega_info_usuarios
from atualizar_arquivo import gerar_arquivo
from exibir_console import exibir
from tratar_info import tratar_informacao



def exibir_pessoas(registro):

    for func in registro:
        print 'Nome:     ',func[0]
        print 'data:     ',func[1]
        print 'hora:     ',func[2]
        print 'Status:   ',func[3]
        print 'Ramal:    ',func[4]
        print '=========================******'


def buscar_func(nome, tempo):

    # retorna lista com as informações dos funcionarios da intranet
    registro = pega_info_usuarios(tempo)

    #registro = [['Davi Roberto de Souza', '2014-07-22', '13:00:00.0', 'Presente', '7241/6297']]
    #            ['Giovanni Abraham Gobo', '2014-07-18', '17:00:00.0', 'Ausente', '7241/6297']]
    
    
    for func in registro:
        if func[0] == nome:
            gerar_arquivo(nome)     # gera os arquivos txt com o nome do funcionario
            tratar_informacao(func) # verifica o status do func para salvar no txt
            
            exibir(func, tempo) # exibi as informações no console
            
            

#exibir_pessoas(pega_info_usuarios())
