# -*- coding: utf-8 -*-
from classes.main import Main
from sys import argv
from classes.error_handler import ErrorHandler

import getopt

# Create Object
oErrorHandler=ErrorHandler()
oMain = Main()

if len(argv) > 0:
    try:
        """
            d: debug
            l: log
            h: help
        """
        opts, args = getopt.getopt(argv[1:], 'dlh')
    except getopt.GetoptError as e:
        print oErrorHandler.displayError('COD-001')
        print oErrorHandler.displayError('COD-002', 'INFO')
        exit()
    
    for o, v in opts:
        # show help? and exit
        if o == '-h':
            oMain.showHelp()
            exit()
    
        if o == '-l':
            print ''
    
        # debug mode?
        if o == '-d':
            oMain.bDebug = True


# run script
oMain.run()