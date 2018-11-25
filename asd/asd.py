import os
class asd:
    def __init__(se):
        se.args = os.sys.argv
        se.targ = se.args[1]
        se.args.pop(1)
        exec(f'import asd.{se.targ}.command')
        exec(f'asd.{se.targ}.command.main()')
def main():
    asd()
