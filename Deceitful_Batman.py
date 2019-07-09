dictionnare={'a': 'AAAAA', 'g':'AABBA','n' : 'ABBAA',
    'b':'AAAAB','h':'AABBB','o':'ABBAB'   ,'u' : 'BAABB','v' : 'BAABB'
    ,'c':'AAABA','i':'ABAAA','j':'ABAAA','p':'ABBBA'  , 'w' : 'BABAA'
    ,'d':'AAABB','k':'ABAAB','q':'ABBBB'  , 'x' : ' BABAB'
    ,'e':'AABAA','l':'ABABA','r':'BAAAA'  , 'y' : ' BABBA'
    ,'f':'AABAB','m':'ABABB','s':'BAAAB'  , 'z' : ' BABBB','t':'BAABA'}
cipher_text="NAANAAANNNAANAAAANANANANAAAAAAAANNAANAAANAAANANNAAAAAAAANNNAANAAAAANAANAAAA"
cipher_text=cipher_text.replace("N","B")
print(cipher_text)
tableau=[cipher_text[i:i+5] for i in range(0,len(cipher_text),5)]
print(tableau)
plain_text=""

for ele in tableau:
	for ele1 in dictionnare:
		if dictionnare[ele1]==ele:
			plain_text+=ele1
			break
			
print(plain_text)
#  theflagisnapier