import pyperclip as pclip
import os
class main_class:
    def __init__(self):
        self.tmp=\
        """#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ts for(int tst=1;tst<=tss;++tst)
int main()
{

}"""
    def opterm(self,path):
        os.system(f'start \"{path} && color a\"')

    def quick_make(self,nm=None):
        path = r'c:\users\ahmed\desktop\py\round'
        os.chdir(path)
        if not nm:
            nm='a'
        f=open(f'{nm}.cpp','w')
        print(self.tmp,file=f)
        f.close()
        os.system(f'gvim {nm}.cpp')
        pclip.copy(f'g++ {nm}.cpp')
        # self.opterm(path)


    def just_make(self,exten,name):
        path = 'c:\\users\\ahmed\\desktop\\py\\{}'.format(exten)
        os.chdir(path)
        nm = '{}.{}'.format(name,exten)
        f=open(nm,'w')
        print(self.tmp,file = f)
        f.close()
        os.system(f'gvim {nm}')
        pclip.copy(f'g++ {nm}')
        # self.opterm(path)




