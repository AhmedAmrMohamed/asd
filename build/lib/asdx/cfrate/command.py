import os
def main():
    platform =  os.sys.platform.lower()
    if  'win' in platform:
        from . import filehandles
        filehandles.main()
    else:
        from . import browserhandles
        browserhandles.main()
