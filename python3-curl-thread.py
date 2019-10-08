#!/usr/bin/python3
import threading
from urllib.request import urlopen
import time
import json

def fetch_url(url):
    try:
        html = urlopen(url)
        o = html.getcode()
        print(o)
        if (o != 200):
            print ("not 200")
        else:
            # juest for my api
            obj = json.loads(html.read().decode())
            print(obj['money'])
    except:
        print ("error")
    finally:
        print ("fetched in %ss" % ((time.time() - start)))

start = time.time()
urls = ["http://money.win.com/api/Client/money?UserID=24222"]
i = 0
while i < 50:
    i = i + 1
    urls.append(urls[0])
print ("start")
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
