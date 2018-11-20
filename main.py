#!/usr/bin/python3
import speedtest
import ping
import time
import datetime
import os
from threading import Thread

# apresentação
print('>>>>>>>>>>>>>>> MONITOR-WAN <<<<<<<<<<<<<<<')
print('Create by: L3onix <Leonardo Facundes - leonardo.fm00@gmail.com>\n\n')

# 0-pacotes transmitidos 1-recebidos 2-perdidos% 3-tempo total de teste ms
# 4-rtt min 5-rtt medio 6-rtt max 7-rtt desvio medio
qtd_pacotes = '2000'    #quantidade exigida no trabalho
tmp_into_req = '0.2'    #tempo exigido no trabalho
ip_test = '8.8.8.8'     #ip de teste exigido no trabalho
#teste_ping = ping.test_ping(qtd_pacotes, tmp_into_req, ip_teste)

# 0-ping 1-download 2-upload
server_id = '12730'     #id de teste sugerido no trabalho
#teste_speedtest = speedtest.test_speedtest(server_id)

# TODO: adaptar este método para abrir uma
# thread para cara teste ser executado ao mesmo tempo
# método para iniciar teste
def start_test():
    #criando threads
    thread_1 = Thread(target=ping.test_ping, args=(qtd_pacotes, tmp_into_req, ip_test, ))
    thread_2 = Thread(target=speedtest.test_speedtest, args=(server_id, ))

    thread_1.start()
    thread_2.start()

# loop com timer
# tempo entre testes
time_into_test = 1800   # em segundos (1800seg = 30min)
# numero de repetições
qtd_repeat = 100    #quantidade de repetições pedidas no trabalho

# imprimindo data de início de execução
print('DATA DE INÍCIO DO TESTE: ' + str(datetime.datetime.now()) + '\n')

# apagando arquivos csv
os.remove("ping-test.csv")
os.remove("speedtest-test.csv")

i = 0
while i < qtd_repeat:
    #chamando execução de teste
    start_test()

    #timer
    time.sleep(time_into_test)
    i += 1

# imprimindo data de final de execução
print('\nDATA DE FINAL DO TESTE: ' + str(datetime.datetime.now()))