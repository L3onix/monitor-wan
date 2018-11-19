#imports
import subprocess
import re

#funcao para teste ping
def test_ping(qtd_pacotes: str, tmp_into_req: str, ip_test: str) -> list:
    #executando comando ping
    ping = str(subprocess.check_output(['ping', '-c', qtd_pacotes, '-i', tmp_into_req, ip_test]))
    #extraindo somente valores
    ping_edit = re.search(r'.{2}packets.*', ping)
    ping_edit = re.sub(r'[a-z/,\\=\'%]', " ", ping_edit.group(0))
    ping_edit = re.findall(r'(\d*\.?\d*\S)', ping_edit)

    #teste
    print ("1 - Thread ping_test")
    for x in ping_edit:
        print(x)

    #TODO: escrever lista de valores em arquivo csv

    #retornando vetor str
    return ping_edit

