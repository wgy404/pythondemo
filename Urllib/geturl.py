import urllib.request
import ssl
context = ssl._create_unverified_context()

keywd = "吴国友"
url = "http://www.baidu.com/s?wd=hello"
key_code = urllib.request.quote(keywd)

url_all = url + key_code

req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req, context=context).read()
fhandle = open("/Users/gavin/Documents/pythondemo/Urllib/1.html", "wb")
fhandle.write(data)
fhandle.close()
