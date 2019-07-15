import urllib.request
import urllib.parse

import ssl
context = ssl._create_unverified_context()

url = "https://www.iqianyue.com/mypost"
# postdata = urllib.parse.urlencode(
#    {"name": "admin", "pass": "passwd"}).encode('utf-8')
# header = headers = {
#    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
req = urllib.request.Request(url)

data = urllib.request.urlopen(req, context=context).read()

fhandle = open("/Users/gavin/Documents/pythondemo/Urllib/2.html", "wb")

fhandle.write(data)

fhandle.close()
