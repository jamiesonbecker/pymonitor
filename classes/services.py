# -*- coding: utf-8 -*-
from socket import socket
from urllib2 import urlopen, HTTPError, URLError
from ftplib import FTP
from helpers import Helpers

class Services:

    oHelpers = ""
    servicesChecksFunc = {}
    listDebugResultOk = []
    listDebugResultError = []
    listTextResultOk = []
    listTextResultError = []
    sErrorFlag = 'error'

    def __init__(self):
        """	Constructor """
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
            self.saveExecuteResult(info)
        except Exception as e:
            self.saveExecuteResult(info, self.sErrorFlag, e)


    def checkHttpService(self, info):
        """ Check HTTP services """
        sUrl = self.oHelpers.formatToValidUrl(info[2])
        try:
            urlopen(sUrl, None, 5).read()
            self.saveExecuteResult(info)
        except (HTTPError, URLError) as e:   
	    self.saveExecuteResult(info, self.sErrorFlag, e)


    def checkFtpService(self, info):
      """ Check FTP services """
        sServer=info[2]
        sPort=info[3]
        sUser=info[4]
        sPassw=info[5]
        try:
	  ftp=FTP()
	  ftp.connect(sServer, sPort)
	  ftp.login(sUser, sPassw)
	  ftp.quit()
	  self.saveExecuteResult(info)
	except Exception as e:
	  self.saveExecuteResult(info, self.sErrorFlag, e)


    def saveExecuteResult(self, info, status="ok", error=""):
        """ Save in diferents list results, Error List and Ok List """
        sResultDebug = self.oHelpers.printOutput(info, status, error)
        sResultText = self.oHelpers.printOutput(info, status, error, 'text')
        if status == 'ok':
	  self.listDebugResultOk.append(sResultDebug)
	  self.listTextResultOk.append(sResultText)
        elif status == self.sErrorFlag:
	  self.listDebugResultError.append(sResultDebug)
	  self.listTextResultError.append(sResultText)
        