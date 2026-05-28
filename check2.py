import urllib.request
import re

html = urllib.request.urlopen('https://neolearn-edtech-platform.vercel.app').read().decode('utf-8')
m = re.search(r'src="(/assets/index-[^"]+\.js)"', html)
if m:
    js = urllib.request.urlopen('https://neolearn-edtech-platform.vercel.app' + m.group(1)).read().decode('utf-8')
    match = re.search(r'https://neolearn-edtech-platform\.onrender\.com[^"\'`]*', js)
    if match:
        print('EXACT URL IN JS:', repr(match.group(0)))
    else:
        print('NOT FOUND IN JS')
else:
    print("Could not find index.js")
