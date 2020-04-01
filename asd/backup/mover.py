import os
class Mover():
    def __init__(self,src,dist):
        print(dist)
        assert os.path.isdir(dist), 'dest dir not found'
        distlist = os.listdir(dist)
        for smt in os.listdir(src):
            if not smt in distlist:
                print(f'copying {smt}')
                os.system(f"cp -r \"{smt}\" \"{dist}/{smt}\"")
