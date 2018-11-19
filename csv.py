import csv

def escrever_arquivo(nome_arquivo: str, dados: list):
    #abrindo ou cirando arquivo
    arquivo = open(nome_arquivo, 'r')
    if(arquivo.read() != ''):
        arquivo = open(nome_arquivo, 'a')
        arquivo.write('\n')
    arquivo = open(nome_arquivo, 'a')

    #escrevendo arquivo
    