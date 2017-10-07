from chatterbot.logic import LogicAdapter
import chatterbot
import json
import random
import re
from urllib import request


class YouKuLogicAdapter(LogicAdapter):

    def __init__(self,**kwargs):
        super(YouKuLogicAdapter,self).__init__(**kwargs);
        self.__get_play_url();

    def can_process(self,statement):
        if(len(re.findall(r"第\d+集",statement.text))>0):
            return True;
        else:
            return False;

    def __get_play_url(self):
        url="http://so.iqiyi.com/so/q_huoyingrenzhe"
        req=request.Request(url);
        web=request.urlopen(req).read().decode("utf-8");
        web=web[web.find("十多年前"):web.find("疾风传")]
        #web='data-searchpingback-elem="link" data-searchpingback-param="ptype=1-3-690" href="http://so.iqiyi.com/links/qcAdm6fzqd2Da5AHK1fa8BDhJW4urKgQIHz85YBHppljzphZ40X5javNfct2avWLHXtWYqtuv8ky0WnmQocBrQ==" data-pb="rtgt=youku&p2=9000" title="第690集" data-tvlist-elem=""     >'
        res=re.findall(r'href="(.+?)"\s+data-pb=".+?9000"\s+title="(第.+?集)"\s+data-tvlist-elem',web);
        #print(res);

        self.dic={};
        for i in range(len(res)): self.dic[res[i][1]]=res[i][0];
        #print(self.dic);


    def process(self, statement):
        confidence=1.0;
        select_statement=statement;
        select_statement.confidence=confidence;
        select_statement.text=self.dic[statement.text[statement.text.index("第"):statement.text.index("集")+1]];
        return select_statement;


bot = chatterbot.ChatBot("Naruto Chatbot",logic_adapters=[
    {'import_path' : "chatbot.YouKuLogicAdapter" },
    {'import_path' : 'chatterbot.logic.best_match.BestMatch'}]);

# bot=chatterbot.ChatBot("9");

bot.set_trainer(chatterbot.trainers.ListTrainer);

with open("data.json","r",encoding="utf-8") as file:
    data=json.load(file)

data=data[:10000];

bot.train(data);


# print(bot.get_response("九尾"));




