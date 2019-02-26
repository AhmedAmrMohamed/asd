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

    def quick_upload():
        pass

    methods = {
            '-h':get_help,
            '-i':quick_install,
            '-u':quick_upload
            }
    methods[option]()

