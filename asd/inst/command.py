import os
def main():
    option = os.sys.argv[1]
    def get_help():
        '''print this help method'''
        for key in methods:
            print(key,methods[key].__doc__)

    def quick_install():
        '''run the python setup.py install'''
        os.system('python setup.py install')

    def asd_install():
        '''install the latest asd proj'''
        path = os.getcwd()
        path = path.replace('\\','/')
        os.chdir('C:\\Users\\Ahmed\\Desktop\\py\\asd')
        os.system('asd inst -q')
        os.chdir(path)

    def quick_upload():
        pass

    methods = {
            '-h':get_help,
            '-q':quick_install,
            '-a':asd_install,
            '-u':quick_upload
            }
    methods[option]()

