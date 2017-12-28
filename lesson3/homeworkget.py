import os

f = open('namelist.txt')
ls = f.readlines() #获得文件中的内容
f.close()
def clone（path）

    name = path.split('/')[-2]
    os.mkdir(name)
    os.system('git clone %s %s'%(i+'.git',name))

