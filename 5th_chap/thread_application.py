from urllib.request import urlopen
import threading
sites=[
    "http://www.baidu.com",
    "http://www.bing.com",
    "http://www.tencent.com",
    # "http://stackoverflow.com",
    # "http://facebook.com",
    # "http://twitter.com"
]

def check_http_status(url):
    return urlopen(url).getcode()

class HTTPStatusChecker(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.status = None
    def getURL(self):
        return self.url
    def getStatus(self):
        return self.status
    def run(self):
        self.status = urlopen(self.url).getcode()

# http_status = {}
# for url in sites:
#     http_status[url] = check_http_status(url)
# print(http_status)


threads = []
for url in sites:
    t = HTTPStatusChecker(url)
    t.start()
    threads.append(t)
for t in threads:
    t.join()

for t in threads:
    print(f"{t.url}: {t.status}")