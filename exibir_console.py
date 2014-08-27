#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from busca_info_intranet import atualizacao_sistema
import ctypes, sys
from contabilizar_horas_trab import gerar_total_horas_trab, info
from datetime import datetime
from atualizar_arquivo import gerar_arq_tot_hr_trab
from contabilizar_horas_trab import hora_atual, data
from calc_horas_mes import soma_tot_mes, tot_mes
import platform


so = platform.system() 

def printColorizedInWindows(text, color):
    """
    0 = Black          1 = Blue            2 = Green
    3 = Aqua           4 = Red             5 = Purple
    6 = Yellow         7 = White           8 = Gray
    9 = Light Blue     10 = Light Green    11 = Light Aqua
    12 = Light Red     13 = Light Purple   14 = Light Yellow
    """
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)
    # cor padrão é 7, white
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)


def exibir_horarios(nome):

    from contabilizar_horas_trab import info

    dados = info(nome).split('/')[2:]

    tam = len(dados)

    in1  = '--:--'
    out1 = '--:--'
    in2  = '--:--'
    out2 = '--:--'

    
    if tam == 1:
        in1 = dados[0]
    if tam == 2:
        in1 = dados[0]
        out1 = dados[1]
    if tam == 3:
        in1 = dados[0]
        out1 = dados[1]
        in2 = dados[2]
    if tam == 4:
        in1 = dados[0]
        out1 = dados[1]
        in2 = dados[2]
        out2 = dados[3]
    
    return [in1,out1,in2,out2]
    
def exibir(func, tempo):

    #data = data()
    hr_atualizacao = atualizacao_sistema() # hora atualizacao do sistema
    tot_hr = gerar_total_horas_trab(func[0]) # calculo das horas trab do func

    nome = func[0]
    data = func[1]
    horas = exibir_horarios(nome)
    
    cor = []
    if func[3] == 'Presente':
        cor = [2]
    else:
        cor = [8]

    if tempo > 30:
        tempo = 0


    print '============================================================='
    print 'Proxima atualizacao:',30-int(tempo),'mim','       Total trab mes:',soma_tot_mes(nome)
    print '\n',nome
	
    if so == 'Windows':
        print 'Status: ',printColorizedInWindows(str(func[3]), cor)
    else:
        if cor[0] == 2:
            color = 'green'
            print 'Status: ',colored(str(func[3]), color)
        else:
            from termcolor import colored
            color = 'grey'
            print 'Status: ',colored(str(func[3]), color)

    print 'Ramal:', func[-1]
    print '\nRegistro         Manha           Tarde'
    print data+'   ',horas[0],horas[1],'   ',horas[2],horas[3],
    print '   Trabalhado:',tot_hr
    print '============================================================='

    
    gerar_arq_tot_hr_trab([data,nome,tot_hr])

