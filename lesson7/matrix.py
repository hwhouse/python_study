import numpy as np
import matplotlib.pyplot as plt

[sin, cos, pi] = np.sin, np.cos, np.pi
'''
def scaletest():

    xys = np.array([(1,1),(2,3),(5,2)]).T
    scale = np.array([[2,0],[0,2]])
    print(np.dot(scale,xys))
scaletest()

def rotate(a):
    xys = np.array([(1,0),(2,0)]).T
    M = np.array([[cos(pi/4),-sin(pi/4)],[sin(pi/4),cos(pi/4)]])
    print(np.dot(M,xys))
'''


def ellipse(b, a, thi):
    ange = np.linspace(0, np.pi * 2, 100)
    xs = np.cos(ange) * 1
    ys = np.sin(ange) * 1
    pts = np.array([xs, ys])
    scale = np.array([[a, 0], [0, b]])
    m = np.array([(cos(thi), -sin(thi)), (sin(thi), cos(thi))])
    pts = np.dot(m, np.dot(scale, pts))
    # print(pts[0].shape)
    plt.gca().set_aspect('equal')
    plt.plot(pts[0], pts[1])
    plt.show()


ellipse(3,5,pi/6)
