#ex1. 思考下面这段程序会输出什么并亲自试一试
def func(x):
    print (x)
    return x+1

x = 2
print (func(x))
#结果: 2 , 3 
#ex2. 创建函数
# 创建一个函数 func，有一个参数 param
# 将输入参数的数值乘以2，作为返回值

def func(param):
    return param*2
    

p = func(20)
print(p)
#ex3. 实现一个函数，输入参数是两个列表，输出返回值是两个列表元素合并并排序后的结果，比如combine([1,5,3], [2,6,7,4])
#返回结果[1,2,3,4,5,6,7]
def funclist(lst1,lst2):
    lst=lst1+lst2
    lst.sort()
    
    return lst
lst1=[1,2,4,5,7,6,30]
lst2=[8,6,3,54,67,123]
print(funclist(lst1,lst2))