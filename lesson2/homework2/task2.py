# 找出100之内的质数
for i in range(2,101):
    for a in range(2,i+1):
        if i%a == 0: break
    if a == i:
        print(i)
        

# 得出斐波那切数列的前100项， 并且输出第99项与第100项的比值
#print('请输入总共项数')
m = int(input('请输入总共项数:'))
a = 0; b = 1
for i in range(1,m+1):
    print(b)
    s = b
    b = a + b
    a = s
print ('最后两项的比值:',a/b)



