from console_color_syntax import ConsoleColorSyntax
from sys import argv


class ErrorHandler:

    oConsoleColor=''
    headerType = {}
    errorDesc={
        'cod-001': ' Uso incorrecto de parametros.',
        'cod-002': ' Ejecute \'python %s -h\' para ver la documentacion.\r\n'\
            % argv[0] ,
        'cod-003': ' No hay servicios para monitorizar, configurelos',
        'cod-004': 'Imposible mostrar la ayuda, intente nuevamente '+ \
                    'y asegurese que el archivo \'docs/help\' exista'
    }
    sCodNotFound=' El codigo de error \'%s\' no se encuentra parametrizado'+\
                    ', consulte al administrador del sistema'

    def __init__(self):
        self.oConsoleColor=ConsoleColorSyntax()
        """the next dictionary contain the "error type" like a Key and
            function to execute like a value
            """
        self.headerType={
            'error': self.oConsoleColor.colorErrorForeBack("[ERROR]"),
            'warning': self.oConsoleColor.colorWarningForeBack('[WARNING]'),
            'info': self.oConsoleColor.colorInfoForeBack("[INFO]")
        }

    def displayError(self, cod, type='error'):
        type = type.lower() #error, warning, info
        cod = cod.lower() # ex: cod-001
        return self.headerType[type] + \
                self.errorDesc.get(cod, self.sCodNotFound % cod)
