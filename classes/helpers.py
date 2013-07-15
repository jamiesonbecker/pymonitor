# -*- coding: utf-8 -*-
from console_color_syntax import ConsoleColorSyntax
from datetime import datetime

class Helpers:
  
  sNow = datetime.now()
  
  def printOutput(self, info, status, error, outputype='console'):
    """ Create debug console/email output """
    
    #Create instance of ConsoleColorSyntax
    oCcs=ConsoleColorSyntax()
    #Get type
    sServiceType=info[1]

    sBody = " Tipo de servicio: "+sServiceType+"\r\n"
    if sServiceType=='tcp':
      sBody +=" Ip: "+info[2]+"\r\n"+ \
		 " Puerto: "+str(info[3])+"\r\n"
    elif sServiceType=='http':
      sBody +=" Url: "+self.formatToValidUrl(info[2])+"\r\n"
	
    if status == "ok":
      if outputype=='console':
	aHeader = oCcs.colorOkForeBack("[RUNNING]") + "\r\n"
	sBody +=" Estado: "+ oCcs.colorOkForeBack("Running") +"\r\n"
      else:
	aHeader = "[RUNNING] \r\n"
	sBody +=" Estado: Running \r\n"
    else:
      if outputype=='console':
	aHeader = oCcs.colorErrorForeBack("[ERROR]") + "\r\n"
	sBody +=" Estado: "+ oCcs.colorErrorForeBack("Error") +"\r\n"\
		" Error: "+ oCcs.colorErrorForeBack(str(error))+"\r\n"
      else:
	aHeader = "[ERROR] \r\n"
	sBody +=" Estado: Error \r\n"\
		" Error: " + str(error)+"\r\n"
	
    return aHeader + sBody

    
  def formatToValidUrl(self, sUrl):
    """ if url have not http://, put this string before"""
    sValidHttp="http://"
    if sUrl[:7]!=sValidHttp:
      return sValidHttp + sUrl
    else:
      return sUrl
      
  def getTimeToFileName(self):
    """Returns the date in the format 15-07-2013_11-01-20 """
    return self.sNow.strftime("%d-%m-%Y_%H-%M-%S")
    
  def getTimeToText(self):
    """Returns the date in the format 15-07-2013 11:12 """
    return self.sNow.strftime("%d-%m-%Y %H:%M")