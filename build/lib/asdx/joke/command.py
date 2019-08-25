import os
from . import joke
def main():
    obj  = joke.main_class()
    argv = os.sys.argv
    try:
        if argv[1]=='get':
            obj.scrape()
        else:
            print(obj.tell())
    except Exception as exc:
        print(exc)
        obj.dummy()

