import os


def help(self,options):
    '''
    -h     no args
           print avilable options(this msg)
    '''
    # print(__doc__)
    for opt in options:
        print(options[opt].__doc__)


