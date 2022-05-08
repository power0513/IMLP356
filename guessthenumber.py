from itertools import count
from typing import Counter


Max = 100
Min =0
#print('請輸入',Min,'<?<',Max,'範圍內的數字:,end=')
#guess=int(input())
ans = 40
while True:
    print('請輸入',Min,'<?<',Max,'範圍內的數字:',end='')
    guess=int(input())
    count += 1
    if guess == ans: 
        print ('BINGO!')
        break

    elif guess>ans:
        print('再小一點,你猜了%d次'%(count))
    else:
        print('再大一點,,你猜了%d次'%(count))
