import csv

def escrever_arquivo(nome_arquivo: str, dados: list):
    #abrindo ou cirando arquivo
    arquivo = open(nome_arquivo, 'a')

    #escrevendo arquivo
    with open(nome_arquivo, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(dados)
        