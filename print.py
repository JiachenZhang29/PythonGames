


'''
#=====================换行指令=======================用\n
massage='你好，\n我叫xxx，\n几岁了。'
print(massage)

#=====================换行指令2======================用三引号
massage='''
'''
你好，
我叫xxx，
几岁了
'''
'''
print(massage)

#======================切片======================

a="ABCDEFGHIJK"
#  012345678910
print(a[::-1])

#=================%f小数点后，四舍五入==================可写%.（小数点几位）f
a=1235.567
print('a%.1f'%a)

#=============%s 字符串站位符  %d 数字站位符 ===============
name='xxx'
age=12
print("我叫%s,我%d岁了"%(name,age))

#====================={}站位符  format() ===============
a=2
b='hello'
massage='我{}岁了,{}'.format(a,b)
print(massage)


name='哈哈'
print('你好，我叫{}。'.format(name))

#大小写函数
#capitalize() title() istitle() upper() isupper() lower() islower()
a='wo shi yi tou zhu'


b=a.capitalize() #将字母的第一个字母大写
print(b)

c=a.title()#每个字母开头大写
print(c)

d=c.istitle()#判断是否每个单词首字母大写
print(d)

e=a.upper()#将字母全部换成大写
print(e)

j=e.isupper()#判断是否字母都是大写
print(j)

f=a.lower()#将字母全部换成小写
print(f)

i=f.islower()#判断是否字母都是小写
print(i)
'''
code=""
s="hfiu43yewhf2454jhds2342aufyehwhjdsayufe862562576"
import random
for x in range(4):
    a=random.randint(1,len(s)-1)
    code+=s[a]
print('验证码:'+code)