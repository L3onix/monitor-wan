#imports
import subprocess
import re

#funcao para teste speedtest
def test_speedtest(id_server: str) -> list:
    #executando comando speedtest
    speedtest = str(subprocess.check_output(['speedtest', '--simple', '--server', id_server]))
    #extraindo somente valores
    speedtest_edit = re.findall(r'(\d*\.\d*)', speedtest)

    #teste
    print("2 - Thread speed_test")
    for x in speedtest_edit:
        print(x)

    #TODO: escrever lista de valores em arquivo csv

    #retornando vetor str
    return speedtest_edit