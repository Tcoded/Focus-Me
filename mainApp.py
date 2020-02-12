import time
from datetime import datetime as dtm

hosts = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
blockList = ["www.facebook.com", "www.youtube.com", "www.twitter.com"]

while True:
    if  ( dtm(dtm.now().year, dtm.now().month, dtm.now().day, 9)
        < dtm.now()
        < dtm(dtm.now().year, dtm.now().month, dtm.now().day, 17)):
        print("Get to work!")
    else:
        print("Get off work!")
    time.sleep(10)