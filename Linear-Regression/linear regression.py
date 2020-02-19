# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:38:58 2020

@author: Student
"""
import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    n=np.size(x)
    m_x, m_y=np.mean(x), np.mean(y)
    SS_xy = np.sum(y*x) -n*m_y*m_x
    print(SS_xy)
    SS_xx = np.sum(x*x) -n*m_x*m_x
    print(SS_xx)
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    return(b_0, b_1)

def plot_regression_line(x,y,b):
    plt.scatter(x,y,color="RED", marker="o", s=30)
    plt.savefig("line_plot.jpg")
    plt.show()
    y_pred = b[0] + b[1]*x
    plt.plot(x,y_pred,color = 'ORANGE')
    plt.xlabel('x-direction')
    plt.ylabel('y-direction')
    plt.scatter(x,y,color="GREEN", marker="o", s=30)
    plt.savefig('graph.jpg')
    plt.show()
    
def main():
    x=np.array([0,2,4,6,7,8,10,11,12,13])
    y=np.array([1,3,5,6,7,8,10,12,13,14])
    b=estimate_coef(x,y)
    print("estimated coefficients:\nb_0={} \nb_1={}".format(b[0],b[1]))
    plot_regression_line(x,y,b)
    
    
if __name__ == "__main__":
    main()
