#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryFile
from xlwt import Workbook, XFStyle
from contabilizar_horas_trab import tot
import os

dados = []
dic = {'01':'Janeiro',
           '02':'Fevereiro',
           '03':'Março',
           '04':'Abril',
           '05':'Maio',
           '06':'Junho',
           '07':'Julho',
           '08':'Agosto',
           '09':'Setembro',
           '10':'Outubro',
           '11':'Novembro',
           '12':'Dezembro'}

def data_mes(data):
    ''' Retorna nome mes'''
    
    mes = data.split('-')[1]

    return dic[mes]

def pega_mes_registro(info):

    valor = info.split('/')[0]
    return data_mes(valor)    

def apagar_excel():
    raiz = 'C:\\Users\\VIT33\\Desktop\\horario trabalho\\Giacomini'
    arquivo = 'Registro.xls'
    try:
        os.remove(os.path.join(raiz, arquivo))
    except WindowsError:
        pass

def pegar_meses_registrados():
    aux = []
    for item in dados:
        if len(item.split('/')) == 6:
            aux.append(pega_mes_registro(item))

    #elimina itens repetidos
    l = list(set(aux)) 
    num_mes = []
    out_list = []

    #gera lista aux com numeros dos meses para ordenacao
    for mes in l:
        for value in dic:
            if mes == dic[value]:
                num_mes.append(value)

    # ordena lista de saida em ordem de mes
    num_mes.sort()
    for i in num_mes:
        out_list.append(dic[i])

    return out_list

def gerar():

    apagar_excel()
    ler_arq_registro()
    if pegar_meses_registrados():
        book = Workbook()
           
        for mes in pegar_meses_registrados():
            escrever_sheet(book, mes)
        book.save('Registro.xls')
        book.save(TemporaryFile())

def escrever_sheet(book, mes):

    sheet = book.add_sheet(mes)
    
    horz_center = XFStyle()
    horz_center.alignment.HORZ_CENTER

    sheet.col(0).width = 5000
    sheet.write(1,0,'Data', horz_center) #(linha, col, dado)
    sheet.col(1).width = 5000
    sheet.write(1,1,'Entrada', horz_center) #(linha, col, dado)
    sheet.col(2).width = 5000
    sheet.write(1,2,'Saida', horz_center) #(linha, col, dado)
    sheet.col(3).width = 5000
    sheet.write(1,3,'Entrada', horz_center) #(linha, col, dado)
    sheet.col(4).width = 5000
    sheet.write(1,4,'Saida', horz_center) #(linha, col, dado)
    sheet.col(5).width = 5000
    sheet.write(1,5,'Total', horz_center) #(linha, col, dado)
    
    linha = 2
    for item in dados:

        if len(item.split('/')) == 6:
            data, nome, in1, out1, in2, out2 = item.split('/')
            if mes == pega_mes_registro(data):
                total = tot(in1, out1, in2, out2)
                sheet.write(linha, 0, data)
                sheet.write(linha, 1, in1)
                sheet.write(linha, 2, out1)
                sheet.write(linha, 3, in2)
                sheet.write(linha, 4, out2)
                sheet.write(linha, 5, total)
                linha += 1
    
def ler_arq_registro():
    arq = open('Davi_Roberto_de_Souza.txt', 'r')

    for linha in arq.read().split('\n'):
        if linha != '':
            dados.append(linha)

    arq.close()

