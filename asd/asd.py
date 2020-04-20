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
        try:
            exec(f'import asd.{se.targ}.command')
            exec(f'asd.{se.targ}.command.main()')
        except ModuleNotFoundError:
            print('unknow script')
        except SyntaxError:
            print('I cannot understand this command\n\
            \rtry agian, for example:\n\
            \rasd sds')
        except KeyboardInterrupt:
            print('... Exiting, see you soon ...')
def main():
    asd()
