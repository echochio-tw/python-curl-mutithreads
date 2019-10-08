import threading
import time
import json

def fetch_url(url):
    from subprocess import call, Popen, PIPE
    try:
        p = Popen(['curl', url ,'--silent'], stdout=PIPE)
        for line in p.stdout:
           print (line)
        p.wait()
    except:
        print ("error")
    finally:
        print ("fetched in %ss" % ((time.time() - start)))

i = 0
start = time.time()
urls = ["http://money.win.com/api/Client/money?UserID=24222"]
while i < 10:
    i = i + 1
    urls.append(urls[0])

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
