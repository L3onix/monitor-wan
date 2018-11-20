#imports
import subprocess
import re
import escrevecsv
import datetime

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
    escrevecsv.escrever_arquivo('ping-test.csv', ping_edit)

    #retornando vetor str
    return ping_edit

