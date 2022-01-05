import OlivOS
import OlivOSCheck

import sys
import json
import os


class Event(object):
    def init(plugin_event, Proc):
        global checkresult
        global checkflag
        if not os.path.exists("plugin/data/OlivOSCheck"):
            os.mkdir("plugin/data/OlivOSCheck")
        if not os.path.exists("plugin/data/OlivOSCheck/finalCheck.json"):
            with open(r"plugin/data/OlivOSCheck/finalCheck.json","w",encoding="utf-8")as file:
                file.write("")
        if not os.path.exists("plugin/data/OlivOSCheck/CheckList.json"):
            jsonput={
                    "CheckList": [
                        "https://github.com/OlivOS-Team/OlivaDiceCore",
                        "https://github.com/OlivOS-Team/OlivaDiceJoy",
                        "https://github.com/OlivOS-Team/OlivaDiceLogger",
                    ],
                    "SendQQ": ""
                    }
            with open(r"plugin/data/OlivOSCheck/CheckList.json","w",encoding="utf-8")as file:
                json.dump(jsonput, file,indent=4,ensure_ascii=False)
        try:
            checkresult=OlivOSCheck.OlivOSCheck.check.GetCheck()
            checkflag=1
            if checkflag==1:
                with open(r"plugin/data/OlivOSCheck/finalCheck.json","w",encoding="utf-8") as file:
                    json.dump(checkresult, file,indent=4,ensure_ascii=False)
        except:
            checkflag=0
            checkresult={}
        
    def init_after(plugin_event, Proc):
        pass
    def private_message(plugin_event, Proc):
        if checkflag==1:
            global lencheck
            lencheck=0
            try:
                checkresult=OlivOSCheck.OlivOSCheck.check.GetCheck()
            except Exception as e:
                checkflag ==0
            with open(r"plugin/data/OlivOSCheck/finalCheck.json","r",encoding="utf-8") as file:
                file=file.read()
                file=json.loads(file)
                if len(checkresult["CommitSave"]) !=len(file["CommitSave"]) :
                    
                    lencheck=1
                for z in file["CommitSave"]:
                    for x in checkresult["CommitSave"]:
                        check=0
                        if list(z.values())[0][0] == list(x.values())[0][0]:
                            check=1
                            break
                    if check!=1:
                        output=str(list(z.keys())[0]).split('/')
                        user=output[-3]
                        repo=output[-2]
                        output='[{}]的[{}]'.format(user,repo)
                        if checkresult["SendQQ"]!="":
                            plugin_event.send('private',checkresult["SendQQ"],output+"更新了"+str(list(z.values())[0][1]))
                        else:
                            plugin_event.reply("请在plugin\data\OlivOSCheck\CheckList.json中将SendQQ修改"+output+"更新了"+str(list(z.values())[0][1]))
                        with open(r"plugin/data/OlivOSCheck/finalCheck.json","w",encoding="utf-8") as file:
                            json.dump(checkresult, file,indent=4,ensure_ascii=False)
            if lencheck==1:
                plugin_event.send('private',checkresult["SendQQ"],r"已检测到CheckList更新,本插件默认您已不准备更新您未更新的版本")
                with open(r"plugin/data/OlivOSCheck/finalCheck.json","w",encoding="utf-8") as file:
                    json.dump(checkresult, file,indent=4,ensure_ascii=False)

    def group_message(plugin_event, Proc):
        pass

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass

# def unity_reply(plugin_event, Proc):
#     if plugin_event.data.message == '/bot' or plugin_event.data.message == '.bot' or plugin_event.data.message == '[CQ:at,qq=' + str(plugin_event.base_info['self_id']) + '] .bot':
#         plugin_event.reply('OlivOSPluginTemplate')

# def poke_reply(plugin_event, Proc):
#     if plugin_event.data.target_id == plugin_event.base_info['self_id']:
#         plugin_event.reply('OlivOSPluginTemplate')
#     elif plugin_event.data.target_id == plugin_event.data.user_id:
#         plugin_event.reply('OlivOSPluginTemplate')
#     elif plugin_event.data.group_id == -1:
#         plugin_event.reply('OlivOSPluginTemplate')

