d="YHAOANUTDSYOEOIEUTTC"
import time
start=0
lenght=len(d)
plain=""
j=0
for i in range(len(d)):
	plain+=d[(start+j)%lenght]
	j+=3
	time.sleep(0.1)
	print(plain)
# YOUSEETHATYOUCANDOIT!
