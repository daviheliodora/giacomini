#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from status_trabalho import buscar_func
from contabilizar_horas_trab import calc_tempo, dif_horas, hora_atual
import time
from os import system
import platform
from gerar_excel import gerar as gerar_excel
from funcionarios import lista_nomes

hora_base = '7:00'

funcionarios = lista_nomes()
                

def limpar_tela():
    so = platform.system()
    if so == 'Windows':
        system("cls")
    else:
        system("clear")

def inicio(hora_base):

    while True:
        limpar_tela()

        hora = dif_horas(hora_base, hora_atual()) # diferença entre hora base e hora atual
        tempo = calc_tempo(hora)

        
        # se hora atual >= a 19h00 encerra o programa
        if hora_atual().split(':')[0] == '19':
            
            import sys
            sys.exit(0)

        #verifica se passou 30 minutos para atualizar aquivo da intranet
        if tempo > 30:
            hora_base = hora_atual()
            gerar_excel()
            

        for funcionario in funcionarios:
            buscar_func(funcionario, tempo)        
        

        time.sleep(60)
	

inicio(hora_base)
    
