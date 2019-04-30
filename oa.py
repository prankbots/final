from lineX import *
from akad.ttypes import *
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import LoginRequest
from akad import LineService
import json, requests
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit
_session = requests.session()
Server_v1 = "BIZANDROID 1.7.2 ANDROID OS 8.1.0"
me = LINE("token oa ",appName=Server_v1)
me.log("Auth Token : " + str(me.authToken))
channelToken = me.getChannelResult()
oepoll = OEPoll(me)
meProfile = me.getProfile()
meSettings = me.getSettings()
meMD = me.profile.mid
mid = me.getProfile().mid
settings = {
    "key": False,
    "teks": "none"
}
def logError(text):
    me.log("eror: " + str(text))
    time_ = datetime.now()
    with open("err.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["key"] == True:
        if pesan.startswith(settings["teks"]):
            Pbot = pesan.replace(settings["teks"],"")
        else:
            Pbot = "Undefined teks"
    else:
        Pbot = text.lower()
    return Pbot
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 26:
            msg = op.message
            text = msg.text
            Id = msg.id
            Key = settings["teks"].title()
            if settings["key"] == False:
                 Key = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if msg._from != me.profile.mid:
                        to = msg._from
                    else:
                        to = msg.to
                elif msg.toType == 1:
                    to = msg.to
                elif msg.toType == 2:
                    to = msg.to
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        Pbot = command(text)
                        if Pbot == "tes":
                          try:
                            me.sendMessage(to,"OK.")
                          except Exception as e:
                            me.log("Eror : " + str(e))
                        if Pbot == "kontak":
                            me.sendContact(to,meMD)
                        if Pbot == "gambar":
                            me.sendImageWithURL(to,"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02")
                        if Pbot == "video":
                            me.sendVideoWithURL(to,"https://avatars0.githubusercontent.com/u/33993971?s=460&v=4")
                        if Pbot == "audio":
                            me.sendAudioWithURL(to,"http://rindra.yn.lt/ringupin/betul.mp3")
        if op.type == 13:
            try:
                group = me.getGroup(op.param1)
                contact = me.getContact(op.param2)
                me.acceptGroupInvitation(op.param1)
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)
        
        if op.type == 59:
            print (op)
        
#==============================================================================#
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        me.log("[SINGLE_TRACE] ERROR : " + str(e))
