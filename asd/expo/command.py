def main():
    import os
    platform = os.sys.platform
    path     = os.getcwd()
    command  = 'xdg-open' if platform == 'linux' else 'explorer'
    os.system(' '.join([command,path]))
