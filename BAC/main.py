def bno(x):return not x
def func1(li):
    # print(li)
    a,b,c,d = map(lambda x:bool(x),li)
    return b&a&c+b&c&d+bno(a)&d
def func2(li):
    a,b,c,d = map(lambda x:bool(x),li)
    return bno(d)&bno(d)|(a&b&c)|(bno(a)&b&d)

# def ok(x,y):
    # for i in zip(x,y):
        # if i[0] != i[1]:
            # return False
    # return True

for i in range(16):
    li = [i&8,i&4,i&2,i&1]
    # print(li)
    li = list(map(lambda x:bool(x),li))
    if(func1(li)!=func2(li)):
        print(li)



