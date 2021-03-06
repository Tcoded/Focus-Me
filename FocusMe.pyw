import time
from datetime import datetime as dtm

hosts = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
blockList = ["www.facebook.com", "www.youtube.com", "www.twitter.com"]

while True:
    if  ( dtm(dtm.now().year, dtm.now().month, dtm.now().day, 9)
        < dtm.now()
        < dtm(dtm.now().year, dtm.now().month, dtm.now().day, 17)):
        with open(hosts, 'r+') as file:
            hostsContent = file.read()
            for site in blockList:
                if site in hostsContent:
                    pass
                else:
                    file.write("#" + " " + redirect + " " + site + '\n')
    else:
        with open(hosts, 'r+') as file:
            hostsContent = file.readlines()
            file.seek(0)
            for line in hostsContent:
                if not any(site in line for site in blockList):
                    file.write(line)
            file.truncate()
    time.sleep(10)