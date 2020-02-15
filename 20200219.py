#ex1. 计算圆面积
# math 模块中的 pi 属性是圆周率π
import math
import random

# 圆面积公式 S = π * r * r
r = 20

# 计算半径为 r 的圆面积
S =math.pi*(r*r)
print(S)
#ex2. 生成10个随机数，输出里面最大的数
l=[]
for i in range(10):
    num1=random.randint(0,100)
    l.append(num1)
    l.sort()
print(l)
print(l[-1])


#ex3. 将第六课（while循环）练习1的猜数字小游戏中的数字用一个1-100之间的随机数来改写，并在猜中后输出猜了几轮猜中答案
num = random.randint(0,101)
count=0
print('Guess what I think?')
while True:
    answer = int(input('please enter a number:'))
    count+=1
    if answer<num:
        print ('too small!')
    if answer>num:
        print ('too big!')
    if answer==num:
        print ('BINGO!,you takes %d times to guess it!'%(count))
        break
