# 洗衣流程
#print('请输入水位')
#level = input()

def wash(level):
    if level=='high':
        print('注水50L')
        print('搅拌60min')
        print('放水')
    elif level=='low':
        print('注水20L')
        print('搅拌30min')
        print('放水')
    

#甩干流程
#print('请输入次数')
#times = int(input())
def dry(times):
    for i in range(times):
        print('注水30L')
        print('搅拌5min')
        print('放水')
        print('高速搅拌')

wash('high')
dry(1)
