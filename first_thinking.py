import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen




# list of investors or links

# bonsai partners - Andrew Rosenblum - https://www.bonsaipartners.com/investor-letters
# -> code in shell: wget -q "https://www.bonsaipartners.com/investor-letters" | cat investor-letters | md5sum
# -> md5sum 28.04.2021: 
#ed0a3895f18c58949867fcd693fbbf65
#d41d8cd98f00b204e9800998ecf8427e

# 1 Main Capital - - https://www.1maincapital.com/materials
# -> code in shell: wget -q "https://www.1maincapital.com/materials" | cat materials | md5sum
# -> md5sum 28.04.2021: d5c8e0e157f0f71ae8ef0a8f4de711ed

def check_link_if_update(link, hash):
	response = urlopen(link).read()
	currentHash = hashlib.sha224(response).hexdigest()

	print('the link: ' + str(link) + ' has actual the following hash:')
	print(str(currentHash))
	return


bonsai_link = 'https://www.bonsaipartners.com/investor-letters'
one_main_capital_link = 'https://www.1maincapital.com/materials'

investor_links = [bonsai_link, one_main_capital_link]


for i in investor_links:
	check_link_if_update(i, 0)


print('finished without errors')
