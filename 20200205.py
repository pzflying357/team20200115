# -*- coding: utf-8 -*-
#ex1. 计算100以内所有3的倍数的和
num=0
for i in range(1,101):
    if i%3==0:
        #print(i)
        num=num+i
print(num)

# ex2
h=int(input('请输入高：'))
w=int(input('请输入宽：'))
for i in range(h):
    for j in range(w):
        print('* ',end='')
    print()

# ex3

for i in range(1, 10):
    for j in range(1,i+1):
        print('%d * %d = %d' % (i, j, i * j), end=' ')
    print()

#跳出循环ex4
nums = [23, 45, 8, 13, 50, 43, 21]
# 把 nums 里的值从前向后累加
# 当总和超过 100 时则不再继续累加
sum = 0
for n in nums:
    # 累加
    sum+=n
    if sum > 100:
        break
# 满足条件时跳出循环
print(sum)