# NarutoChatbot

Naruto Chatbot 是一个基于日本动漫《火影忍者》进行训练的微信自动聊天机器人。它基于python实现，可以处理微信聊天中的私聊和群聊的文字消息，并且针对不同关键词进行特殊的回复,比如发送《火影忍者》特定集数的优酷播放超链接，或者回复一张图片等。<br><br>

![image](https://github.com/maxichu/NarutoChatbot/raw/master/cover.jpg)


## How it works
Naruto Chatbot使用了chatterbot, itchat， nstools等开源项目(包）。项目整体的结构框架如下：<br><br>

<div align=center><img src="https://github.com/maxichu/NarutoChatbot/raw/master/framework.jpg" /> </div><br><br>

主要分为三层，预处理层，聊天机器人层和微信接口层。<br>

预处理层主要完成的工作包括：<br>
1.使用python将下载的原始字幕文件批量重命名，转换文件格式后存储为训练字幕文件。<br>
2.使用nstools对文件中的繁体字进行简体转换。<br>
3.将训练字幕文件进行对白提取，抛弃header、timeline等信息，以json格式存储为训练数据。<br>

聊天机器人层使用Chatterbot包，负责对输入字符串进行处理，给出回复信息，具体思路如下：<br>
1.抓取优酷视频搜索"火影忍者"的结果界面，抓取每一集的url和第X集信息，保存到python的dictionary中。<br>
2.添加Logistic Adapter，如果检测到用户输入中有"第XX集"，则返回优酷该集动漫的播放链接。<br>
3.添加Best Match Adapter，如果没有检测到"第XX集"，则调用Best Match方法进行回复消息生成。<br>
4.使用训练数据对模型进行训练，得到聊天消息生成模型。<br>

微信接口层使用itchat包，负责对微信聊天信息的监听，并调用聊天消息生成模型得到消息后发送，具体思路如下：<br>
1.弹出二维码，扫描登录微信。<br>
2.绑定两个decorator对群聊和私聊消息进行监听。<br>
3.如果检测消息中有"火影忍者"，则发送一张主题海报图片。<br>
4.将字符串输入到聊天消息生成模型，得到回复语句并发送。<br>

## Performance
运行效果如下面四张图所示：<br>

<table><tr>
<td><img src="https://github.com/maxichu/NarutoChatbot/raw/master/P1.PNG" width="405" height="720" border=0></td>
<td><img src="https://github.com/maxichu/NarutoChatbot/raw/master/P2.PNG" width="405" height="720" border=0></td>
</tr></table>

<table><tr>
<td><img src="https://github.com/maxichu/NarutoChatbot/raw/master/P3.PNG" width="405" height="720" border=0></td>
<td><img src="https://github.com/maxichu/NarutoChatbot/raw/master/P4.PNG" width="405" height="720" border=0></td>
</tr></table>

## Future Work
1.使用情景喜剧对白改善聊天机器人回复的精确度。<br>
2.使用DeepLearning方法进行回复消息生成。<br>
3.完善微信接口层的其他功能，比如发送视频，文件等。<br>

<img src="https://github.com/maxichu/NarutoChatbot/raw/master/back_cover.jpg"/>

