n=int(input('输出斐波拉契数列的前n项:n='))
list=[]
for m in range(0,n):
    if m==0:
        list.append(0)
    elif m==1:
        list.append(1)
    else:
        list.append(list[m-1]+list[m-2])
for i in range(len(list)):
    print(list[i],end=' ')