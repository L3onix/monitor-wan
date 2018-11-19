#!/usr/bin/python3
import speedtest
import ping
import time
from threading import Thread

# 0-pacotes transmitidos 1-recebidos 2-perdidos% 3-tempo total de teste ms
# 4-rtt min 5-rtt medio 6-rtt max 7-rtt desvio medio
qtd_pacotes = '4'
tmp_into_req = '0.2'
ip_test = '127.0.0.1'
#teste_ping = ping.test_ping(qtd_pacotes, tmp_into_req, ip_teste)

# 0-ping 1-download 2-upload
server_id = '12730'
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

# TODO: fazer loop com timer e abrir threads para teste simultaneo
# loop com timer
i = 0
while i < 5:
    #chamando execução de teste
    start_test()

    #timer
    time.sleep(60)
    i += 1