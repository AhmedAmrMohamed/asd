import requests as rq
import pickle
import random
import os
class main_class:
    def __init__(self):
        self.path = self.fixed_path()
        self.file = f'{self.path}/jokes'
        self.urla = 'https://corporatebs-generator.sameerkumar.website/'
        self.urlb = 'https://geek-jokes.sameerkumar.website/api'

    def fixed_path(self):
        pa = os.path
        path = pa.normcase(pa.abspath(__file__))
        path = path.split('\\')
        path.pop()
        path = '/'.join(path)
        return path
    def get_two(self):
        a=rq.get(self.urla).json()['phrase']
        b=rq.get(self.urlb).json()
        return a,b

    def scrape(self):
        jokes = set()
        for i in range(20):
            print('getting ',i)
            a,b=self.get_two()
            jokes.add(a)
            jokes.add(b)
        self.add(jokes)

    def add(self,jokes):
        fi = open(self.file,'rb')
        st = pickle.load(file = fi)
        fi.close()
        st.union(jokes)
        fi = open(self.file,'wb')
        pickle.dump(jokes,file = fi)
        fi.close()

    def tell(self):
        fi = open(self.file,'rb')
        jokes = pickle.load(file = fi)
        fi.close()
        joke = random.choice(list(jokes))
        jokes.remove(joke)
        fi = open(self.file,'wb')
        pickle.dump(jokes,file = fi)
        fi.close()
        return joke

    def dummy(self):
        f=open(self.file,'wb')
        pickle.dump(set(),file = f)
        f.close()


