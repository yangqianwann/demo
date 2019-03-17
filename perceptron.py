# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:57:16 2019

@author: YangQianwan
"""
def train(theta,x,y):
    alpha=0.11 #学习率
    for xyi in zip(x,y):
        ir=predict(theta,[xyi[0],])[0]
        if ir==xyi[1]: #如果预测值等于真实值
            pass
        else: #更新参数
            theta[0]+=alpha*(xyi[1]-ir)*xyi[0][0] #更新第一个属性的权值
            theta[1]+=alpha*(xyi[1]-ir)*xyi[0][1] #更新第二个属性的权值
            theta[2]+=alpha*(xyi[1]-ir) #更新偏置值
            predict(theta,x)
            train(theta,x,y)
    return theta

def predict(theta,x):
    r=[]
    for xi in x:
        ir =theta[0]*xi[0]+theta[1]*xi[1]+theta[2]
        if ir>0:
            r.append(1)
        else:
            r.append(-1)
    return r

if __name__=='__main__':
    x=[(1,1),(1,1.8),(1,1.2),(-1,-1),(1,1.7)]
    #x.append(())
    y=[1,1,1,-1,1]
    w=[-0.5,0.6,0.7] 
    w=train(w,x,y)
    r=predict(w,x) 
    print(y)
    print(r)
    
    
