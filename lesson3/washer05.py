# 洗衣流程

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

def dry(times):
    for i in range(times):
        print('注水30L')
        print('搅拌5min')
        print('放水')
        print('高速搅拌')


def wash_dry(obj,level='low',times=1):
    print('===开始洗衣===')
    wash(level)
    dry(times)
    print('%s 洗干净了'%obj) #%s 替换字符串，%f 替换浮点数

wash_dry('衣服')
wash_dry('毛毯','high',3)
wash_dry('被套',times=2)
