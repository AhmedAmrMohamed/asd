import os
class asd:
    def __init__(se):
        se.args = os.sys.argv
        se.targ = se.args[1]
        se.args.pop(1)
        if se.targ == 'drfrilled':
            try:
                import webbrowser
                webbrowser.open('https://www.youtube.com/watch?v=gO8N3L_aERg')
            except Exception as e:
                print('almost there try again later')
            finally:
                quit()
        exec(f'import asd.{se.targ}.command')
        exec(f'asd.{se.targ}.command.main()')
        # if se.targ != 'joke':
            # os.system('asd joke tell')
def main():
    asd()
