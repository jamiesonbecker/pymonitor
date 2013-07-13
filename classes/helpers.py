# -*- coding: utf-8 -*-
from console_color_syntax import ConsoleColorSyntax

class Helpers:
  
  def printOutput(self, info, status, error, outputype='console'):
    """ Create debug console/email output """
    
    #Create instance of ConsoleColorSyntax
    oCcs=ConsoleColorSyntax()
    #Get type
    sServiceType=info[1]

    sBody = "Tipo de servicio: "+sServiceType+"\r\n"
    if sServiceType=='tcp':
      sBody +=" Ip: "+info[2]+"\r\n"+ \
		 " Puerto: "+str(info[3])+"\r\n"
    elif sServiceType=='http':
      sBody +=" Url: "+self.formatToValidUrl(info[2])+"\r\n"
	
    if status == "ok":
      aHeader = oCcs.colorOkForeBack("[RUNNING]") + "\r\n"
      sBody +=" Estado: "+ oCcs.colorOkForeBack("Running") +"\r\n"
    else:
      aHeader = oCcs.colorErrorForeBack("[ERROR]") + "\r\n"
      sBody +=" Estado: "+ oCcs.colorErrorForeBack("Error") +"\r\n"\
	       " Error: "+ oCcs.colorErrorForeBack(str(error))+"\r\n"
	       
    return aHeader + sBody
    
  def formatToValidUrl(self, sUrl):
    """ if url have not http://, put this string before"""
    sValidHttp="http://"
    if sUrl[:7]!=sValidHttp:
      return sValidHttp + sUrl
    else:
      return sUrl