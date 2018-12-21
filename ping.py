#imports
import subprocess
import re
import escreve_csv
import datetime

class Ping:
    # TODO: sobrecarregar contrutor para adaptação futura
    # construtores
    def __init__(self):
        self.__qtd_pacotes = ''
        self.__tmp_into_req = ''
        self.__ip_test = ''
    
    def preenche_dados(self):
        self.__qtd_pacotes = str(input("Quantidade de pacotes: "))
        self.__tmp_into_req = str(input("Tempo entre requisições: "))
        self.__ip_test = str(input("Endereço IP alvo: "))
        #self.confere_dados(self)

    def confere_dados(self):
        print("qtd_pacotes - " + self.__qtd_pacotes)
        print("tmp_into_req - " + self.__tmp_into_req)
        print("ip_teste - " + self.__ip_test)

    def executa_teste(self):
        resultado = str(subprocess.check_output(['ping', '-c', self.__qtd_pacotes, '-i', self.__tmp_into_req, self.__ip_test]))
        resultado = self.corrige_resultado(self, resultado)
        #self.imprime_resultado(resultado)
        escreve_csv.escrever_arquivo('ping-test.csv', resultado)
        
    @staticmethod
    def corrige_resultado(self, resultado) -> list:
        pattern = re.compile('.{' + str(len(self.__qtd_pacotes)+1) + '}packets.*')
        resultado_edit = re.search(pattern, resultado)
        resultado_edit = re.sub(r'[a-z/,\\=\'%]', " ", resultado_edit.group(0))
        resultado_edit = re.findall(r'(\d*\.?\d*\S)', resultado_edit)
        return resultado_edit
    
    @staticmethod
    def imprime_resultado(resultado):
        for x in resultado:
            print(x)



#funcao para teste ping
def test_ping(qtd_pacotes: str, tmp_into_req: str, ip_test: str) -> list:
    #executando comando ping
    ping = str(subprocess.check_output(['ping', '-c', qtd_pacotes, '-i', tmp_into_req, ip_test]))
    #extraindo somente valores
    pattern = re.compile('.{' + str(len(qtd_pacotes)+1) + '}packets.*')
    ping_edit = re.search(pattern, ping)
    ping_edit = re.sub(r'[a-z/,\\=\'%]', " ", ping_edit.group(0))
    ping_edit = re.findall(r'(\d*\.?\d*\S)', ping_edit)

    #teste
    print ("1 - Thread ping_test - " + str(datetime.datetime.now()))
    #for x in ping_edit:
    #    print(x)

    #escrevendo lista de valores em arquivo csv
    escreve_csv.escrever_arquivo('ping-test.csv', ping_edit)

    #retornando vetor str
    return ping_edit

