# -*- coding: utf-8 -*-
from thread import exit

import config.services_list as services
from error_handler import ErrorHandler
from services import Services
from helpers import Helpers
 
class Main:
  
    bDebug = False
    bLog = False
    oServices = ''
    oErrorHandler = ''
    oHelpers = ''
    

    def __init__(self):
        self.oErrorHandler = ErrorHandler()
        self.oHelpers = Helpers()
   
    def run(self):
        """Check services for all servers configs data"""
        if self.validateServicesList():
            self.oServices = Services() #Create Services object
            for info in services.services_list:
                self.oServices.check(info)
            # show debug
            self.showDebugResult()
            # save logs 
            self.saveLogFile()

    def validateServicesList(self):
        """Validate if the services list not empty"""
        bResult=True
        if len(services.services_list) == 0:
            print self.oErrorHandler.displayError('cod-003', 'warning')
            bResult=False

        return bResult
        
      
    def showDebugResult(self):
        """ Show debug, first show Error, then Ok results"""
        if self.bDebug == True:
            for x in self.oServices.listDebugResultError:
                print x
  
            for x in self.oServices.listDebugResultOk:
                print x
        
        
    def saveLogFile(self):
      """Save result in log file"""
      if self.bLog:
	try:
	  fileLog = open('logs/log_'+self.oHelpers.getTimeToFileName(), 'w')
	  fileLog.seek(0)
	  fileLog.write("Fecha y Hora: "+self.oHelpers.getTimeToText()+"\r\n \r\n");
	  for result in self.oServices.listTextResultError:
	    fileLog.write(result)
	  for result in self.oServices.listTextResultOk:
	    fileLog.write(result)
	    
	  fileLog.close()
	except IOError:
	  print self.oErrorHandler.displayError('cod-005')

    def showHelp(self):
        """ Read the help file to show help's script"""
        try:
            sHelp = open('docs/help', 'r').read()
            print sHelp
        except:
            print self.oErrorHandler.displayError('cod-004')
      