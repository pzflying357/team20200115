#ex1
money = 88
if  money > 100:
    print("rich")
else:
    print('poor')
#ex2
#（a）  True
bingo = False
if bingo == False:
    print(True)
else:
    print(False)
#（b） False
b = 3
if b - 3:
    print(True)
else:
    print(False)
#（c） if enter anything print True,else print False
x = input('please enter some words:')
if x:
    print(True)
else:
    print(False)
#（d）
a = True
b = not a
print(b)   #False
print(not b)#True
print(a == b)#False
print(a != b)#True
print(a and b)#False
print(a or b)#True
print(1<2 and b==True)#False