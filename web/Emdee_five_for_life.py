#!/usr/bin/python
import requests,re,hashlib


host="http://docker.hackthebox.eu:38056"
r=requests.session()
s=r.get(host)
has=re.findall("<h3 align='center'>(.*)</h3>",s.text)
print(has[0])
result=hashlib.md5(has[0].encode()) 
hasha=result.hexdigest()
print hasha
data={'hash':hasha}
flag=r.post(url=host,data=data)

print(flag.text)
# the flag is: HTB{N1c3_ScrIpt1nG_B0i!}
