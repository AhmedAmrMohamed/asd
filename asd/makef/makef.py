import os
class main_class:
    def __init__(self):
        self.tmp=\
        """#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{

}"""
    def quick_make(self,nm=None):
        os.chdir(r'c:\users\ahmed\desktop\py\round')
        if not nm:
            nm='a'
        f=open(f'{nm}.cpp','w')
        print(self.tmp,file=f)
        f.close()
        os.system(f'gvim {nm}.cpp')


    def just_make(self,exten,name):
        path = 'c:\\users\\ahmed\\desktop\\py\\{}'.format(exten)
        os.chdir(path)
        nm = '{}.{}'.format(name,exten)
        f=open(nm,'w')
        print(self.tmp,file = f)
        f.close()
        os.system(f'gvim {nm}')



