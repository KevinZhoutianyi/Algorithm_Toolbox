a,b,c = 1 ,2,"wut"

print(type(a))

str = 'QWERTYUIOP'
print(str[0:])


myFirstList = ['it ca n be any type',1,3,45.1]
list2 = [1,2,3,4]
for temp in list2:
    print(temp)


myTuple = ("special list which","cannot be changed")
for each in myTuple:
    print(each)


changeableTuple = (["this is",'a list!'],":","2","3")
changeableTuple[0][1] = ""
for y in changeableTuple:
    print(y,end=',')


dic = {}
dic["iheqwie"] = "hiewhqie"
print(dic.keys())

set_ = {"12313","12313","123"}
for z in set_:
    print(z)


cNum=complex(1.2,3.4)
cNum = 1.3 + 3.4j
print(cNum)


judge = 0
if judge == 1:
    print("1")
elif judge == 2:
    print("2")
elif judge == 3:
    print("3")
else:
    print("0")


for t in range(10,100):
    print(t,end = ',')

print("！@#！#！@")

while (judge)!=0:
    pass 

MyIter = iter(myFirstList)
while 1:
    try:
        print(next(MyIter))
    except StopIteration:
        break


class myIterClass:
    a = 0
    def __iter__(self):
        return self
 
    def __next__(self):
        if(self.a<100):
            self.a += 1
            return self.a
        else:
            raise StopIteration


myIterteTemp = myIterClass()
myInterclass = iter(myIterteTemp)
while 1:
    try:
        print(next(myIterteTemp))
    except StopIteration:
        break



def Fabonaqie(n):
    a,b,counter = 0,1,0
    while 1:
        if(counter>n):
            return
        yield a
        a,b,counter = b,a+b,counter+1
    

f = Fabonaqie(20)
while 1:
    try:
        print(next(f))
    except StopIteration:
        break


def IsIttuple(arg1,**manyArg):
    print(arg1)
    print(type(manyArg))
    print(manyArg)
    for var in manyArg:
        print(var)


IsIttuple(1,a=2,b=3,c=4)


sum = lambda arg1,arg2,arg3: arg1+arg2+arg3

print("!@#!@#!#!",sum(1,2,3))
    
def TestRange():

    qwq = 1
    def TestRange2():
        nonlocal qwq
        qwq = 2 
        print(qwq)
    TestRange2()
    print(qwq)

TestRange()


var = 1
def fun():
    global var
    print(var)
    var = 20
fun()

globalVar = 1
def CanPrint():
    nonLocalVar = 2
    def Internal():
        print(globalVar)
        nonLocalVar = 3
    return Internal

caaaa = CanPrint()
caaaa()
    

        
#闭包就是外函数返回内函数 然后赋值给一个函数对象 然后就可以用内函数了 也开始function(a)(b)
#内函数可以访问外函数和外函数变量 从小试到大的，但如果内函数里新定义了一个同名的变量 那么外变量就不可见了 除非你用nonlocal把内函数的变量指定为外函数的那个变量 或者global指定为全局的
        



