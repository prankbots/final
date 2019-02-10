import lineX
from lineX import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from gtts import gTTS
from googletrans import Translator
_session = requests.session()
botStart = time.time()
sett = codecs.open("set.json","r","utf-8")
gmails = codecs.open("gmail.json","r","utf-8")
plates = codecs.open("template.json","r","utf-8")
set = json.load(sett)
gmail = json.load(gmails)
plate = json.load(plates)
me = LINE(gmail["selfbot"],gmail["password"])
# BATAS POLL
oepoll = OEPoll(me)
meProfile = me.getProfile()
meSettings = me.getSettings()
# BATAS MID
meM = me.getProfile().mid
Bt = [meM]
all = [me]
OWNER = ["u0ac948397fbc732bd3bc5ca273faa698"]
oaBot = ["ub0842532a31b9d99856cf2590b17d33f","udfaf52176415b46cb445ae2757ec85f3","u17a086ccff618e754588a1108335867f","uc8dc5352066b6a344bde3c07b0fe04ea","ub9c30fd47257ec4337ee777657b4df66"]
chim = "uc8dc5352066b6a344bde3c07b0fe04ea"
St = set["stile"]
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
jam = "『 " + timeNow.strftime('%H:%M:%S') + " 』"
for bots in all:
  for addbot in Bt:
    try:
      bots.findAndAddContactsByMid(addbot)
    except:pass
  for addoa in oaBot:
    try:
      bots.findAndAddContactsByMid(addoa)
    except:pass
  for admin in set["admin"]:
    try:
      bots.findAndAddContactsByMid(admin)
    except:pass
def backupData():
  try:
    backup = set
    f = codecs.open('set.json','w','utf-8')
    json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
    backup = gmail
    f = codecs.open('gmail.json','w','utf-8')
    json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
    backup = read
    f = codecs.open('read.json','w','utf-8')
    json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
    return True
  except Exception as e:
    print(e)
    return False
def restartBot():
  print ("RESETTED")
  backupData()
  python = sys.executable
  os.execl(python, python, *sys.argv)
def Comt(text):
  pesan = text.lower()
  if set["Key"] == True:
    if pesan.startswith(set["text"]):
      Pbot = pesan.replace(set["text"],"")
    else:
      Pbot = "Undefined command"
  else:
    Pbot = text.lower()
  return Pbot
def bot(op):
  global threading
  global groupParam
  opp1 = op.param1
  opp2 = op.param2
  opp3 = op.param3
  try:
    if op.type == 0:
      return
    if op.type == 25:
      msg = op.message
      text = msg.text
      Id = msg.id
      Key = set["text"].title()
      if set["Key"] == False:
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
            Pbot = Comt(text)
            # TEMPLATE
            if Pbot == "price":
              me.sendFlex(to, plate["pricelist"])
            elif Pbot == "listapp":           
              me.sendFlex(to, plate["listapp1"])
              me.sendFlex(to, plate["listapp2"])
            elif Pbot == "help":
              me.sendFlex(to, plate["help"])
            elif Pbot.startswith("pictlab "):
              separate = text.split(" ")
              teks = text.replace(separate[0] + " ","")
              url1 = "https://memegen.link/buzz/"+teks+".jpg"
              url2 = "https://memegen.link/joker/"+teks+".jpg"
              url3 = "https://memegen.link/cbg/"+teks+".jpg"
              url4 = "https://memegen.link/fry/"+teks+".jpg"
              url5 = "https://memegen.link/yuno/"+teks+".jpg"
              url6 = "https://memegen.link/fa/"+teks+".jpg"
              url7 = "https://memegen.link/iw/"+teks+".jpg"
              url8 = "https://memegen.link/blb/"+teks+".jpg"
              url9 = "https://memegen.link/doge/"+teks+".jpg"
              url10 = "https://memegen.link/firsttry/"+teks+".jpg"
              data = {
                "type": "template",
                "altText": "SendgifPicture",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": url1,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url2,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url3,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url4,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url5,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url6,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url7,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url8,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url9,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": url10,
                      "action": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95",
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
              me.sendFlex(to, data)
            elif Pbot == "memberlist":
              if msg.toType == 2:
                group = me.getGroup(to)
                ret_ = "╭━━━══[ Member List ]"
                no = 0 + 1
                for mem in group.members:
                  ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                  no += 1
                ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                warnanya1 = random.choice(warna1)
                data = {
                    "type": "flex",
                    "altText": "{} membagikan aplikasi".format(meProfile.displayName),
                    "contents": {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": str(ret_),
                                    "wrap": True,
                                    "color": warnanya1,
                                    "align": "center"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [{
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                    "type": "uri",
                                    "label": "OPEN CHANNEL",
                                    "uri": "line://app/1623679774-9GWpqpGw"
                                    }													
                                },
                            {
                                "type": "spacer",
                                "size": "sm",
                            }],
                            "flex": 0
                        }
                    }
                }
                me.sendFlex(to, data)
            elif Pbot == "memberpict":
              kontak = me.getGroup(to)
              group = kontak.members
              picall = []
              for ids in group:
                if len(picall) >= 400:
                  pass
                else:
                  picall.append({
                    "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                    "action": {
                      "type": "uri",
                      "uri": "http://line.me/ti/p/~adiputra.95"
                      }
                    }
                  )
              k = len(picall)//10
              for aa in range(k+1):
                data = {
                  "type": "template",
                  "altText": "{} membagikan janda".format(meProfile.displayName),
                  "template": {
                    "type": "image_carousel",
                    "columns": picall[aa*10 : (aa+1)*10]
                  }
                }
                me.sendFlex(to, data)
            elif Pbot == "pendinglist":
              if msg.toType == 2:
                group = me.getGroup(to)
                ret_ = "╭━━━══[ Pending List ]"
                no = 0 + 1
                if group.invitee is None or group.invitee == []:
                  me.sendMessage(to, "Tidak ada pendingan")
                  return
                else:
                  for pen in group.invitee:
                    ret_ += "\n{}. {}".format(str(no), str(pen.displayName))
                    no += 1
                    ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                  warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                  warnanya1 = random.choice(warna1)
                  data = {
                    "type": "flex",
                    "altText": "{} membagikan aplikasi".format(meProfile.displayName),
                    "contents": {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": str(ret_),
                                    "wrap": True,
                                    "color": warnanya1,
                                    "align": "center"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [{
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                    "type": "uri",
                                    "label": "OPEN CHANNEL",
                                    "uri": "line://app/1623679774-9GWpqpGw"
                                    }													
                                },
                            {
                                "type": "spacer",
                                "size": "sm",
                            }],
                            "flex": 0
                        }
                    }
                  }
                  me.sendFlex(to, data)
            elif Pbot == "myprofile":
              contact = me.getContact(msg._from)
              cover = me.getProfileCoverURL(msg._from)
              me.reissueUserTicket()
              res = "╭━━━━profile info━━━\n"
              res += St+"Display Name :{}\n".format(contact.displayName)
              res += St+"Mid: {}\n".format(contact.mid)
              res += St+"Status Message\n"+St+"{}\n".format(contact.statusMessage)
              me.sendMessage(to, res)
              try:
                poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
              except:
                poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
              dax = {
                "type": "template",
                "altText": "berak di celana",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": poto,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "PROFILE",
                        "uri": poto,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": cover,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "COVER",
                        "uri": cover,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": "https://qr-official.line.me/L/"+me.getUserTicket().id+".png",
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "CONTACT",
                        "uri": "https://line.me/ti/p/"+me.getUserTicket().id,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
              me.sendFlex(to, dax)
            elif Pbot == "me":
              h = me.getContact(msg._from)
              me.reissueUserTicket()
              data = {
               "type": "flex",
               "altText": "{} cangkemu".format(str(h.displayName)),
               "contents": {
                "type": "bubble",
                "styles": {
                  "header": {
                    "backgroundColor": "#333300",
                  },
                  "body": {
                    "backgroundColor": "#333333",
                    "separator": True,
                    "separatorColor": "#ffffff"
                  },
                  "footer": {
                    "backgroundColor": "#333333",
                    "separator": True
                  }
                },
                "header": {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "™ᴛᴇᴀᴍ ᴘʀᴀɴᴋʙᴏᴛ™",
                      "weight": "bold",
                      "color": "#00ffff",
                      "size": "xxl"
                    }
                  ]
                },
                "hero": {
                  "type": "image",
                  "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "uri": "https://line.me/ti/p/~adiputra.95"
                  }
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "md",
                  "action": {
                    "type": "uri",
                    "uri": "https://line.me/ti/p/~adiputra.95"
                  },
                  "contents": [
                    {
                      "type": "text",
                      "text": "━━━━━━╦℘яᴀɴᴋ™ʙøᴛ╦━━━━━━",
                      "size": "md",
                      "color": "#00ffff"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "baseline",
                          "contents": [
                            {
                              "type": "icon",
                              "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                              "size": "5xl"
                            },
                            {
                              "type": "text",
                              "text": "Name : ",
                              "weight": "bold",
                              "color": "#008B8B",
                              "margin": "sm",
                              "flex": 0
                            },
                            {
                              "type": "text",
                              "text": h.displayName,
                              "size": "sm",
                              "align": "end",
                              "color": "#aaaaaa"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "baseline",
                          "contents": [
                            {
                              "type": "icon",
                              "url": "https://avatars0.githubusercontent.com/u/33993971?s=460&v=4",
                              "size": "5xl"
                            },
                            {
                              "type": "text",
                              "text": "Creator",
                              "weight": "bold",
                              "color": "#008B8B",
                              "margin": "sm",
                              "flex": 0
                            },
                            {
                              "type": "text",
                              "text": "Acil",
                              "size": "sm",
                              "align": "end",
                              "color": "#aaaaaa"
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "baseline",
                          "contents": [
                            {
                              "type": "icon",
                              "url": "https://raw.githubusercontent.com/Aprank/logo/master/20181215_052531.png",
                              "size": "5xl"
                            },
                            {
                              "type": "text",
                              "text": "REPOSITORY",
                              "margin": "sm",
                              "color": "#008B8B",
                              "weight": "bold",
                              "flex": 0
                            },
                            {
                              "type": "text",
                              "text": "PRANKBOTS",
                              "size": "sm",
                              "align": "end",
                              "color": "#aaaaaa"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "text",
                      "text": "________________________________________________\nmy whatsup : 085719122254",
                      "wrap": True,
                      "color": "#aaaaaa",
                      "size": "xxs"
                    }
                  ]
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "spacer",
                      "size": "sm"
                    },
                    {
                      "type": "button",
                      "style": "primary",
                      "color": "#10CF08",
                      "action": {
                        "type": "uri",
                        "label": "MY CONATCT",
                        "uri": "https://line.me/ti/p/"+me.getUserTicket().id
                      }
                    }
                  ]
                }
               }
              }
              me.sendFlex(to, data)
  except Exception as e:
    print(e)
    if op.type == 59:
      print(op)
while True:
  try:
    ops=oepoll.singleTrace(count=50)
    if ops != None:
      for op in ops: 
        bot(op)
        oepoll.setRevision(op.revision)       
  except Exception as e:
    me.log("EROR WHILE TRUE\n" + str(e))
