import requests
from time import sleep
from datetime import date,datetime, time
while True:
	t=datetime.now().time()
	print(t)
	if (t>time(9,00) and t<time(9,10)):
		k=3
	else:	
		send_text = 'https://stocklock.herokuapp.com/'
		response = requests.get(send_text)
		print(response)
	sleep(500)	