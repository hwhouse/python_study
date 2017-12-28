import numpy as np
import matplotlib.pyplot as plt
'''
def vectordot():
    v1 = np.array([3,0])
    v2 = np.array([2,3])
    print(np.dot(v1,v2))
    
vectordot()

def vectorcross():
    v1 = np.array([3,0])
    v2 = np.array([2,3])
    print(np.cross(v1,v2))

def triarea(p1,p2,p3):
    v1 = np.array(p2)-np.array(p1)
    v2 = np.array(p3)-np.array(p1)
    print(np.abs(np.cross(v1,v2))/2)

def polyarea(xys):
    print(np.abs(np.cross(xys[:-1],xys[1:]).sum())/2)
'''
#triarea((0,0),(5,0),(0,-2))
a = np.linspace(0,np.pi*2,100)
xs = np.cos(a)*1
ys = np.sin(a)*1
plt.gca().set_aspect('equal')
plt.plot(xs,ys)
plt.show()
#polyarea(np.array([xs,ys]).T)

