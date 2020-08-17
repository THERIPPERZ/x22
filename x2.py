from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
vvv = []
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)

import urllib.parse

class NewQRLogin:
    API_URL = "https://api.lrtt.icu/secondaryQrCodeLogin.do"
    HEADERS = {
        "android_lite": {
            "User-Agent": "LLA/2.12.0 SKR-H0 9",
            "X-Line-Application": "ANDROIDLITE\t2.12.0\tAndroid OS\t9;SECONDARY"
        },
        "android": {
            "User-Agent": "Line/10.6.2",
            "X-Line-Application": "ANDROID\t10.6.2\tAndroid OS\t10"
        },
        "ios_ipad": {
            "User-Agent": "Line/10.1.1",
            "X-Line-Application": "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5"
        },
        "ios": {
            "User-Agent": "Line/10.1.1",
            "X-Line-Application": "IOS\t10.1.1\tiPhone 8\t11.2.5"
        },
        "chrome": {
            "User-Agent": "MozilX-Line-Application/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "X-Line-Application": "CHROMEOS\t2.3.2\tChrome OS\t1"
        },
        "desktopwin": {
            "User-Agent": "Line/5.12.3",
            "X-Line-Application": "DESKTOPWIN\t5.21.3\tWindows\t10"
        },
        "desktopmac": {
            "User-Agent": "Line/5.12.3",
            "X-Line-Application": "DESKTOPMAC\t5.21.3\tMAC\t10.15"
        }
    }

    def parseLogin(this, loginInfo):
        return (loginInfo["token"], loginInfo["certificate"])

    def loginWithQrCode(self, header, certificate="", callback=lambda output: print(output)):
        assert header in self.HEADERS, "invaild header"
        resp = requests.post(self.API_URL + "/login?" + urllib.parse.urlencode({"custom_headers": self.HEADERS[header], "certificate": certificate}))
        res = resp.json()
        if resp.status_code != 200:
            raise Exception(res)
        callback("Login URL: %s" % (res["url"]))

        while "token" not in res:
            resp = requests.post(self.API_URL + res["callback"])
            res = resp.json()
            if resp.status_code != 200:
                raise Exception(res)

            if "pin" in res:
                callback("Input PIN: %s" % (res["pin"]))

        return self.parseLogin(res)

    def loginQrCodeWithWebPinCode(self, header, certificate="", callback=lambda output: print(output)):
        assert header in self.HEADERS, "invaild header"
        resp = requests.post(self.API_URL + "/login?" + urllib.parse.urlencode({"custom_headers": self.HEADERS[header], "certificate": certificate}))
        res = resp.json()
        if resp.status_code != 200:
            raise Exception(res)
        callback("Pincode URL: %s" % (res["web"]))
        callback("Login URL: %s" % (res["url"]))

        while "token" not in res:
            resp = requests.post(self.API_URL + res["callback"])
            res = resp.json()
            if resp.status_code != 200:
                raise Exception(res)

        return self.parseLogin(res)

qrv2 = NewQRLogin()
token, cert = qrv2.loginQrCodeWithWebPinCode("ios_ipad")
wait = {
    "mnm":True,
    "yyy":True,
    "zzz":True,
    "cudow":False,
    "mes8":{},
    "number":{},
    "mess":{},
    "img1":{},
    "img2":{},
    "img3":{},
    "img4":{},
    "ct":{},
    "img5":{},
    "img6":{},
    "autoJoinTicket":False,
    "delay":{}
}
help = """คำสั่ง

.m1 [ข้อความ] ส่งข้อความทุกกลุ่ม
.m2 [ข้อความ] ส่งข้อความหาเพื่อน
.c1 [mid] ส่งคอนแท็กทุกกลุ่ม
.c2 [mid] ส่งคอนแท็กหาเพื่อน

.help ดูคำสั่ง
.test เช็คบอท
.speed เช็คความไว
.sendpost [ID โพส] แชร์โพส
.uid (@) ขโมย mid
.post:ไอดีโพส:จำนวนรอบ

.mm สั่งโปร
.img1 (ลิงค์รูป)
.img2 (ลิงค์รูป)
.img3 (ลิงค์รูป)
.img4 (ลิงค์รูป)
.img5 (ลิงค์รูป)
.img6 (ลิงค์รูป)
.ct (mid)
.settext (ข้อความ) ตั้งข้อความ
.setdelay (จำนวน) ตั้งดีเลย์
.setnumber (จำนวน) ตั้งรอบ"""

APP = "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5"
APPS = 'ANDROIDLITE'
botStart = time.time()
cl = LINE(token,appName=APP)
#cl = LINE(appName=APP)
print(cl.authToken)
clm = cl.profile.mid;poll = OEPoll(cl)

admin = [clm]

def logError(text):
    cl.log("ERROR : " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendall():
    sx = cl.getGroupIdsJoined()
    if wait["img1"] == {}:
        for ak in [ak for ak in sx if not ak in vvv]:
            cl.sendMessage(ak,wait["mes8"])
            time.sleep(0.2)
    else:
        for ak in [ak for ak in sx if not ak in vvv]:
            cl.sendMessage(ak,wait["mes8"])
            time.sleep(0.2)
            cl.sendImageWithURL(ak,wait["img1"])
            time.sleep(0.2)
            cl.sendImageWithURL(ak,wait["img2"])
            time.sleep(0.2)
            cl.sendImageWithURL(ak,wait["img3"])
            time.sleep(0.2)
            cl.sendImageWithURL(ak,wait["img4"])
            time.sleep(0.2)
            cl.sendImageWithURL(ak,wait["img5"])
            time.sleep(0.2)
            cl.sendImageWithURL(ak,wait["img6"])
            time.sleep(0.2)
            cl.sendContact(ak,wait['ct'])
            time.sleep(0.2)
 #           cl.sendMessage(ak,wait["mes8"])
#            time.sleep(0.2)
def altarcall(op):
    global wait
    global admin
    try:
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            elif msg.text.lower() == 'set on':
                    if msg.to in vvv:
                        cl.sendMessage(msg.to,"เปิดอยู่แล้ว")
                    else:
                        vvv.append(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        #print(vvv)
                        cl.sendMessage(msg.to,"เปิด")
            elif msg.text.lower() == 'set off':
                    if msg.to in vvv:
                        vvv.remove(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.unsendMessage(msg_id)
                    else:
                        cl.sendMessage(msg.to,"ปิด")
            elif msg.text.lower().startswith('.post:'):
                if msg._from in admin:
                    list_ = msg.text.split(":")
                    post = list_[1]
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        cl.sendPostToTalk(msg.to,post)
                    cl.sendMessage(msg.to, "แชร์โพสไปแล้วจำนวน {} ครั้ง".format(number))
            elif msg.text.lower().startswith(".sendpost "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    contacts = cl.getGroupIdsJoined()
                    for contact in contacts:
                        cl.sendPostToTalk(contact,tastk)
                        
            elif msg.text.lower().startswith(".img1 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["img1"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าขรูปสำเร็จ\n\n' + tastk)
                    
            elif msg.text.lower().startswith(".img2 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["img2"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าขรูปสำเร็จ\n\n' + tastk)
                    
            elif msg.text.lower().startswith(".img3 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["img3"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าขรูปสำเร็จ\n\n' + tastk)

            elif msg.text.lower().startswith(".img4 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["img4"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าขรูปสำเร็จ\n\n' + tastk)
            elif msg.text.lower().startswith(".img5 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["img5"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าขรูปสำเร็จ\n\n' + tastk)
            elif msg.text.lower().startswith(".img6 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["img6"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าขรูปสำเร็จ\n\n' + tastk)
            elif msg.text.lower().startswith(".ct "):
                if msg._from in admin:
                     tastk = " ".join(msg.text.split(" ")[1:])
                     wait["ct"] = tastk
                     cl.sendMessage(msg.to,'ตั้งค่า คท. สำเร็จ\n\n' + tastk)

            elif msg.text.lower().startswith(".settext "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["mes8"] = tastk
                    cl.sendMessage(msg.to,'ตั้งค่าข้อความสำเร็จ\n\n' + tastk)
            elif msg.text.lower().startswith(".setnumber "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["number"] = int(tastk)
                    cl.sendMessage(msg.to,'ตั้งค่าจำนวนรอบสำเร็จ:\n\n' + tastk)
            elif msg.text.lower().startswith(".setdelay "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["delay"] = int(tastk)
                    cl.sendMessage(msg.to,'ตั้งค่าดีเลย์สำเร็จ:\n\n' + tastk)
            elif msg.text.lower().startswith(".mm"):
               if msg._from in admin:
                    if wait["mes8"] == {}:
                        cl.sendMessage(msg.to,"โปรดตั้งข้อความ จำนวนรอบ และ ดีเลย์ก่อน")
                    else:
                        for x in range(int(wait["number"])):
                            sendall()
                            time.sleep(int(wait["delay"]))
                        cl.sendMessage(msg.to,'ส่งข้อความสำเร็จ')
            elif msg.text.lower().startswith(".speed"):
               if msg._from in admin:
                    start = time.time()
                    cl.sendMessage(msg.to, "กำลังทดสอบ...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(msg.to,format(str(elapsed_time)))
            elif msg.text.lower().startswith(".help"):
               if msg._from in admin:
                    cl.sendMessage(msg.to,help)

            elif msg.text.lower().startswith(".m1 "):
               if msg._from in admin:
                    def cudows():
                        if wait["cudow"] == False:
                            contacts = cl.getGroupIdsJoined()
                            cl.sendMessage(msg.to,'กำลังส่งข้อความ โปรดรอสักครู่')
                            for contact in contacts:
                                cl.sendMessage(contact,wait["mess"])
                                time.sleep(0.3)
                            wait["cudow"] = True
                            cl.sendMessage(msg.to,'ส่งข้อความสำเร็จ')
                        else:
                            cl.sendMessage(msg.to,'โปรดรอสัก 10 นาที\n\nเมื่อถึงเวลากำหนดจะมีข้อความแจ้งเตือน')
                            time.sleep(600)
                            wait["cudow"] = False
                            cl.sendMessage(msg.to,'สามารถใช้งานได้แล้ว')

                    tastk = " ".join(msg.text.split(" ")[1:])
                    wait["mess"] = tastk
                    th = threading.Thread(target=cudows)
                    th.start()

            elif msg.text.lower().startswith(".m2 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    contacts = cl.getAllContactIds()
                    for contact in contacts:
                        cl.sendMessage(contact,tastk)
                        time.sleep(0.3)
                    wait["cudow"] = True
                    cl.sendMessage(msg.to,'ส่งข้อความไปเพื่อนทุกคนสำเร็จ')

            elif msg.text.lower().startswith(".p1 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    sx = cl.getGroupIdsJoined()
                    for ak in sx:
                        cl.sendImageWithURL(ak, tastk)
                        time.sleep(0.8)
                    cl.sendMessage(msg.to,'ส่งรูปไปทุกกลุ่มสำเร็จ')
            elif msg.text.lower().startswith(".p2 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    contacts = cl.getAllContactIds()
                    for contact in contacts:
                        cl.sendImageWithURL(contact,tastk)
                        time.sleep(0.8)
                    cl.sendMessage(msg.to,'ส่งรูปหาเพื่อนทุกคนสำเร็จ')

            elif msg.text.lower().startswith(".c1 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    sx = cl.getGroupIdsJoined()
                    for ak in sx:
                        cl.sendContact(ak, tastk)
                        time.sleep(0.8)
                    cl.sendMessage(msg.to,'ส่ง contact ไปทุกกลุ่มสำเร็จ')
            elif msg.text.lower().startswith(".c2 "):
               if msg._from in admin:
                    tastk = " ".join(msg.text.split(" ")[1:])
                    contacts = cl.getAllContactIds()
                    for contact in contacts:
                        cl.sendContact(contact,tastk)
                        time.sleep(0.8)
                    cl.sendMessage(msg.to,'ส่ง contact ไปเพื่อนทุกคนสำเร็จ')

            elif ".uid " in msg.text.lower():
               if msg._from in admin:
                    spl = re.split(".uid ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = cl.getContact(uid)
                            cl.sendMessage(msg.to,userData.mid)

            elif msg.text.lower().startswith(".test"):
                cl.sendMessage(msg.to,'on')
    except Exception as error:
        logError(error)
def run():
    while True:
        try:
            ops = poll.singleTrace(count=50)
            if ops is not None:
               for op in ops:
                   threads = []
                   for i in range(1):
                       thr = threading.Thread(target=altarcall(op))
                       threads.append(thr)
                       thr.start()
                       poll.setRevision(op.revision)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    run()
