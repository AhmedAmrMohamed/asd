def main():
    import os
    command = None
    if os.sys.platform == 'linux':
        command = 'xdg-open'
    elif os.sys.platform.startswith('win'):
        command = 'explorer'
    else:
        print('unsupported platform')
        quit()

    os.system(f'{command} {os.getcwd()}')
