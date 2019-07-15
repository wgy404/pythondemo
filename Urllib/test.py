from urllib.request import urlopen

import ssl

context = ssl._create_unverified_context()

html = urlopen('https://www.baidu.com/', context=context).read()

fhandle = open("/Users/gavin/Documents/pythondemo/Urllib/2.html", "wb")

fhandle.write(html)

fhandle.close()
