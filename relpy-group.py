import itchat, time
from itchat.content import *

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
    #itchat.send("this is an auto-reply from aposta-VirtualBox",msg['FromUserName']);
    print(msg['FromUserName'])
    dict(msg)


itchat.auto_login(True)
itchat.run()
