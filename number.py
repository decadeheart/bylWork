import random

sNum = random.randint(1, 20)

print('这是一个1~20之间的数字')

guess = 0

while guess != sNum:
    print('请输入猜测的数字')
    guess = int(input())

print('猜对啦')

    
