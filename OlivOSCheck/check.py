import os
import sys
import re
import json
import requests

class Url:
    def __init__(self,user,repo):
        self.sha=None
        self.node_id=None
        self.commit={}
        self.url=None
        self.html_url=None
        self.comments_url=None
        self.author={}
        self.committer={}
        self.parents={}
        self.check=0
        self.user=user
        self.repo=repo

    def GetNew(self):
        user=self.user
        repo=self.repo
        api="https://api.github.com/repos/{}/{}/commits".format(user,repo)
        headers={"Authorization":"token "+"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"}
        #headers={}
        payload={}
        proxies={}
        times=10
        response = requests.request("GET", api, headers=headers, data=payload,timeout=times)
        finaljson = json.loads(response.text)
        if finaljson !="":
            finaljson = json.loads(response.text)[0]
            self.sha=finaljson["sha"]
            self.node_id=finaljson["node_id"]
            self.commit=finaljson["commit"]
            self.url=finaljson["url"]
            self.html_url=finaljson["html_url"]
            self.comments_url=finaljson["comments_url"]
            self.author=finaljson["author"]
            self.committer=finaljson["committer"]
            self.parents=finaljson["parents"]
        return
def GetCheck():
    with open("plugin\data\OlivOSCheck\CheckList.json","r",encoding="utf-8" ) as file:
        file=json.load(file)
        commitsave=[]
        checkresult={}
        for i in file["CheckList"]:
            urlsave={}
            havejson=0
            user=i.split("/")[-2]
            repo=i.split("/")[-1]
            check=0
            url=Url(user,repo)
            api="https://api.github.com/repos/{}/{}/commits".format(user,repo)
            try:
                url.GetNew()
                check=1
            except Exception as e:
                urlsave[api]="ERROR"
                commitsave.append(urlsave)
                continue
            if check ==1:
                urlsave[api]=[url.sha,url.commit["message"]]
                commitsave.append(urlsave)
        checkresult['CommitSave']=commitsave
        checkresult['SendQQ']=file["SendQQ"]
        return checkresult