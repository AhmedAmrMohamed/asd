from . import makef
import os
def main():
    arg = os.sys.argv
    print(arg)
    obj = makef.main_class()
    if len(arg) > 2:
        opt = arg[1]
        if opt == '-m':
            nam = arg[2]
            ext = arg[3]
            obj.just_make(ext,nam)
    else:
        # print(arg)
        nm = arg[1] if len(arg) == 2 else None
        obj.quick_make(nm)
    # os.system('asd expo')

