'''
i=0
while i<10:
    print(i)
================================================================================

n=1
while n<=50:
    if n%3 ==0 and n%5==0:
        print('--------->',n)
    n+=1

n=0
while n<=10:
    print('@'*n)
    n+=1

for x in range(20):
    print("@"*x)
    n+=1

#==============三角形==============

ceng=1
while ceng<=15:
    count=1
    while count<=ceng:
        print('@',end='')
        count+=1
#====层换行====
    print()
    ceng+=1

#============九九乘法表============
i=1
while i <=9:
    count=1
    while count<=i:
        print(str(count)+"*"+str(i)+"="+str(i*count),end=' ')
        count+=1
    print()
    i+=1
'''

        
