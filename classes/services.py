# -*- coding: utf-8 -*-
from socket import socket
from urllib2 import urlopen
from helpers import Helpers

class Services:

    bDebug = False
    oHelpers = ""
    servicesChecksFunc = {}
    listDebugResultOk = []
    listDebugResultError = []
    sErrorFlag = 'error'

    def __init__(self, debug):
        """	Constructor """
        self.bDebug = debug
        self.oHelpers = Helpers()
        self.servicesChecksFunc = {'tcp': self.checkTcpService, \
            'http': self.checkHttpService, \
            'ftp': self.checkFtpService \
        }


    def check(self, info):
        """ General check services """
        self.servicesChecksFunc[info[1]](info)


    def checkTcpService(self, info):
        """ Check TCP services """
        sIp = info[2]
        nPort = info[3]
        try:
            sock = socket()
            #if isinstance(sock, SocketTest):
            sock.connect((sIp, nPort))
            sock.close
            self.saveDebugResult(info)
        except Exception as e:
            self.saveDebugResult(info, self.sErrorFlag, e)


    def checkHttpService(self, info):
        """ Check HTTP services """
        sUrl = self.oHelpers.formatToValidUrl(info[2])
        try:
            urlopen(sUrl, None, 5).read()
            self.saveDebugResult(info)
        except Exception as e:
            self.saveDebugResult(info, self.sErrorFlag, e)


    def checkFtpService(self, info):
        print 'TODO'


    def saveDebugResult(self, info, status="ok", error=""):
        """ Save in diferents list the debug results, Error List and Ok List """
        if self.bDebug == True:
            result = self.oHelpers.printOutput(info, status, error)
            if status == 'ok':
                self.listDebugResultOk.append(result)
            elif status == self.sErrorFlag:
                self.listDebugResultError.append(result)
        