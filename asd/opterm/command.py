import os
def main():
    arg = os.sys.argv
    pa = os.path.normcase(arg[1])
    print(pa)
    os.system(f'start cd {pa}\"')
