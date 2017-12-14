import os
def walk(dirname,i = ''):
    
    for name in os.listdir(dirname):
        path = os.path.join(dirname,name)
        if os.path.isfile(path):
            print(i,name)
        else:
            print(i,name,':')
            walk(path,i=i+'--')
            
