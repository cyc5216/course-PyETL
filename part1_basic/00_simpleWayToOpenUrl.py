# 若為Mac電腦，請先貼上此段程式碼
########### For Mac user ###########
import os
import ssl
# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

# 引入urllib
from urllib import request


url = 'http://ed668677.ngrok.io/hello_get?age=22&name=Allen'

res = request.urlopen(url)

# print('res :',res)
print('res.read() :',res.read())

# Try res.read().decode('utf-8')
# print(res.read().decode('utf8'))
