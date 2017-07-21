import itchat, time
from itchat.content import *
import pandas as pd
import numpy as np

groups=[]
listenTo = ['womendushilanhaizi',
            'beidajianghuai2017']
ids=[]
msgList=[]

'''
initialize the environment , register the id of chatroom which are about to be listened
and then run the program
'''
def initEnvironment():
    itchat.auto_login(hotReload=True)
    groups = itchat.get_chatrooms(update=True, contactOnly=True)
    for dic in groups:
        if dic['PYQuanPin'] in listenTo:
            ids.append(dic['UserName'])
    print('ids are following')
    print(ids)
    itchat.run()

def recordForMsg(msg):
    print('start adding!')
    if msg['Type'] == TEXT:
        content = msg['Content']
    else:
        content = '#OTHER CONTENTS'
    tempTurple=(msg['ActualNickName'],msg['Content'],time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    msgList.append(tempTurple)
    if len(msgList) % 10 == 0 :
        print("numbers come to {}".format(len(msgList)))
        #save to csv
        pd.DataFrame(msgList).to_csv('test.csv',sep=',')

@itchat.msg_register([TEXT, PICTURE, SHARING], isGroupChat=True)
def textCollect(msg):
    if not msg['FromUserName'] in ids:
        print('message : {} from user {} in other chatrooms got! {}'.format(msg['Content'],msg['ActualNickName'],msg['FromUserName']) )
        return
    print('from {NAME} recived message {CONT}'.format(NAME = msg['ActualNickName'],CONT = msg['Content']))
    print('\n')
    recordForMsg(msg)
    


initEnvironment()
    
    
    
    #@@3042d57735ba554791c7e1d6e2c92fed6ceb22f6b4ec785e257a2b565b7b32e7
