import requests
import itchat
import json, time
import chatbot
import chatterbot
import itchat.core as it_msg


KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT, isGroupChat=False)
def bot_reply(msg):
    #mediaID =itchat.upload_file(fileDir="naruto.gif", isPicture=True);
    print(msg.User.NickName);
    if ("火影忍者" in msg["Text"]):
        itchat.send('@img@naruto.gif', msg['FromUserName']);
    return chatbot.bot.get_response(msg["Text"]).text;


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
    print("Message got:", msg["Text"])
    # print( "群名： ", msg.User.NickName )
    # print( "发件人： ", msg.ActualNickName )

    if msg.User.NickName.find("国庆七天") >= 0 or msg.User.NickName.find("浦发银行") >= 0:
        print("这是我们的群！可以回复啊！")
        reply = chatbot.bot.get_response(msg["Text"]).text;
        print("回复在群：", reply)
        #mediaID=itchat.upload_file(fileDir="naruto.gif",isPicture=True);
        if("火影忍者" in msg["Text"]):
            itchat.send('@img@naruto.gif', msg['FromUserName']);
        return reply


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.send('@img@%s' % 'gz.gif',toUserName="Dejavu");
itchat.run()