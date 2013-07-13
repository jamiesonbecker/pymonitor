# -*- coding: utf-8 -*-
from vendors.colorama import init, Fore, Back, Style
init()

class ConsoleColorSyntax:
  
  def colorErrorForeBack(self, string):
    return Style.BRIGHT + Fore.RED + string + self.resetForeBack()
    
  def colorOkForeBack(self, string):
    return Style.BRIGHT + Fore.GREEN + string + self.resetForeBack()
    
  def colorWarningForeBack(self, string):
    return Style.BRIGHT + Fore.YELLOW + string + self.resetForeBack()
    
  def colorInfoForeBack(self, string):
    return Style.BRIGHT + Fore.BLUE + string + self.resetForeBack()
    
  def resetForeBack(self):
    return Back.RESET + Fore.RESET + Style.NORMAL