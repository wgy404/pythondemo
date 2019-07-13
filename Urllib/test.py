import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

for i in range(1, 100):
    try:
        file = urllib.request.urlopen(
            "https://blog.csdn.net/qq_43153313/article/details/90726040",
            timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常—->" + str(e))
