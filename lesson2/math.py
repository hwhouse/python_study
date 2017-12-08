'''
# 求1+2+3+...+100 = ?
s = 0
for i in range(1,101):
    if i%2 == 0: # 判断是否满足条件
        s += i
print(s)

s = 0
for i in range(1,101):
    if i%2 != 0: continue # 满足条件，则不执行下一步直接进入下一次循环
    s += i
print(s)
'''
# break
s,i = 0,0
while True:
    i += 1
    if i%2 == 1: continue
    cs,ci = 0,1
    while ci>0:
        cs += ci%10
        ci //= 10
    if cs == 9:
        s += 1
        print(i)
        if s==7: break

