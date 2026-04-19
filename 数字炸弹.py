import random
import time
boom='''
********************
*                  *
*      BooM!!!     *
*                  *
******************** '''
bomb = random.randint(1, 100)
print(bomb)
start = 0
end = 100
#============================玩家============================
while True:
    people = int(input('请输入{}到{}之间的数:'.format(start, end)))
    if people > bomb:
        print('大了')
        end = people
    elif people < bomb:
        print('小了')
        start = people
    else:
        print(boom)
        break
#============================电脑============================
    print('等待电脑输入{}到{}之间的数:'.format(start, end))
    time.sleep(5)
    computer = random.randint(start + 1, end - 1)
    print('电脑输入：{}'.format(computer))
    if computer > bomb:
        print('大了')
        end = computer
    elif computer < bomb:
        print('小了')
        start = computer
    else:
        print(boom)
        break