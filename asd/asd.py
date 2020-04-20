import os
class asd:
    def __init__(se):
        se.args = os.sys.argv
        se.targ = se.args[1]
        se.args.pop(1)
        if se.targ == 'help':
            li = os.listdir()[:]
            li = list(filter(lambda x: not '.' in x and x[0] != '_', li))
            print('\n'.join(li))
            quit()
        if se.targ == 'drfrilled':
            try:
                import webbrowser
                webbrowser.open('https://www.youtube.com/watch?v=gO8N3L_aERg')
            except Exception as e:
                print('almost there try again later')
            finally:
                quit()
        try:
            exec(f'import asd.{se.targ}.command')
            exec(f'asd.{se.targ}.command.main()')
        except ModuleNotFoundError:
            print('unknow script\ntype "asd help" for optional scripts')
        # if se.targ != 'joke':
            # os.system('asd joke tell')
def main():
    asd()
