# -*- coding: utf-8 -*-
i = 0
while i < 5:
   i += 1
   for j in range(3):
       print (j)
       if j == 2:
           break
   for k in range(3):
       if k == 2:
           continue
       print (k)
   if i > 3:
       break
   print (i)
#ex1
num = 10
while True:
    print('Guess what I think?')
    answer = int(input('please enter a number:'))
    if answer<num:
        print ('too small!')
    if answer>num:
        print ('too big!')
    if answer==num:
        print ('BINGO!')
        break

#ex2
# 输出 1 到 10，但不输出 4 和 5
count = 0
while count < 10:
    count += 1
    if count == 4 or count == 5:
        continue
    print(count)


#ex3 使用 while 计算100以内所有3的倍数的和（即：计算3、6、9 ... 96、99 的和）
num=0
sum=0
while num <100:
    num += 1
    if num %3 == 0:
        sum += num
print(sum)