# 若為Mac電腦，請先貼上此段程式碼
########### For Mac user ###########
import os
import ssl
# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

for i in range(0, 3):
    url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232004767'

    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    json_string = str(soup)
    js = json.loads(json_string)

    last_id = js[len(js)-1]['id']

    for each_article in js:
        print(each_article['title'])
        print('https://www.dcard.tw/f/photography/p/' + str(each_article['id']))
        print()

    url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=%s'%(last_id)
