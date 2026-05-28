import urllib.request
import re

html = urllib.request.urlopen('https://neolearn-edtech-platform.vercel.app').read().decode('utf-8')
m = re.search(r'src="(/assets/index-[^"]+\.js)"', html)
if m:
    js = urllib.request.urlopen('https://neolearn-edtech-platform.vercel.app' + m.group(1)).read().decode('utf-8')
    print('onrender:', 'onrender' in js)
    print('localhost:', 'localhost:5000' in js)
else:
    print("Could not find index.js")
