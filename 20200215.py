# -*- coding: utf-8 -*-
# 1.字典
# 创建一个字典，包含 one、two、three 三个键
# 对应的值分别为 1，2，3
data = {'one':1,'two':2,'three':3}

# 将 two 键对应的值改为 4
data['two']=4

print(data)
#2.统计下这段文字里，不同单词出现的次数
# Beautiful is better than ugly Explicit is better than implicit Simple is better than complex
# Complex is better than complicated Flat is better than nested Sparse is better than dense
sen='Beautiful is better than ugly Explicit is better than implicit Simple is better than complex \
Complex is better than complicated Flat is better than nested Sparse is better than dense'
lst=sen.split()
count={}
for i in lst:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)