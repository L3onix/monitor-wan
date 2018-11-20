#imports
import subprocess
import re
import escrevecsv
import datetime

#funcao para teste speedtest
def test_speedtest(id_server: str) -> list:
    #executando comando speedtest
    try:
        speedtest = str(subprocess.check_output(['speedtest', '--simple', '--server', id_server]))
        
        #extraindo somente valores
        speedtest_edit = re.findall(r'(\d*\.\d*)', speedtest)
    except:
        #caso teste não funcione
        speedtest_edit = ['0', '0', '0']

    #teste
    print("2 - Thread speed_test - " + str(datetime.datetime.now()))
    #for x in speedtest_edit:
    #    print(x)

    # escrevendo lista de valores em arquivo csv
    escrevecsv.escrever_arquivo('speedtest-test.csv', speedtest_edit)

    #retornando vetor str
    return speedtest_edit