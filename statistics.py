import pandas as pd
import numpy as np
import time
import subprocess as sp

def lenByTimes(t):
    name,tt=t
    return tt

#data is Series
def getList(data):
    ddata=data.drop_duplicates()
    lis=[]
    for i in ddata:
        lis.append((i,data.loc[data==i].count()))
    return lis

def getSortedList(lis,keyy=lenByTimes,rev=True):
    return sorted(lis,key=keyy,reverse=rev)

#return the file name
def extractTime(timeData):
    print('extracting time dataset')
    name=time.strftime('%Y-%m-%d',time.localtime(time.time()))+'-timeInfo-.csv'
    df=pd.DataFrame(timeData)
    df.to_csv(name,index=False)
    print('statistics of time written to {}'.format(name))
    return name

def main(dir):
    data=pd.read_csv(dir)
    #counting for members
    print('counting for members')
    lis=getSortedList(getList(data['0']))
    df=pd.DataFrame(lis)
    print(lis)
    day=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    name=time.strftime('%Y-%m-%d',time.localtime(time.time()))+'-memberTimes-.csv'
    df.to_csv(name)
    print('statistics of members written to {}'.format(name))
    #extract time
    name=extractTime(data['2'])
    #time analysis
    sp.Popen(['./analysisTime',name,day])


