num = input()
num = int(num)
print(type(num))

if num % 2==0:
    print('這是偶數')
else:
    print('這是奇數')

#if num % 2 == 1:
#    print('這是奇數')
#else:
#    print('這是偶數')
if num>=1 and num<=1000:
    print('correct')
else:
    print('incorrect')
