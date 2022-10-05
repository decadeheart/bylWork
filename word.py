s = []        #定义一个空列表
count = 0      #定义一个存文本单词数目的变量
while 1:
    a = input()    #文本输入
    if a == '#':    #‘#！’作为输入结束的判断
        break
    b = a.split()    #将输入的文本删除空格存入b
    for i in b:        #遍历b中的单词
        if i not in s:     #b中出现列表s中没有的单词，存入列表s
            count+=1       #新单词数目+1
            s.append(i)

s.sort()     #对列表中的单词进行排序
for j in range(count):
    print(s[j])