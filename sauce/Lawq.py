import urllib.request
import webbrowser
import time
file = "sitedata.html"
url = input('Enter URL : ')
urllib.request.urlretrieve(url, file)
file=urllib.request.urlretrieve(url, file)
print("Data scrape is success.")
time.sleep(1)
