import requests
import json
import numpy as np
import time
from datetime import date,datetime,timedelta

day0=datetime.now()
day1=day0+timedelta(1)
day2=day0+timedelta(2)
day3=day0+timedelta(3)
day4=day0+timedelta(4)
day5=day0+timedelta(5)
day6=day0+timedelta(6)

Week=np.array([day0,day1,day2,day3,day4,day5,day6])

	
#print("date = ", day0.strftime('%d-%m-%Y'))






#print(result.json())




def GetData():
	for x in range(7):
		Date=Week[x].strftime('%d-%m-%Y')
		print(Date)
		url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date={}'.format(Date)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
		result = requests.get(url, headers=headers)
		new_result=result.json()
		num=len(new_result['sessions'])
		num1=num
		for i in range(num):
			print(i+1,new_result['sessions'][i]['center_id'],new_result['sessions'][i]['name'],new_result['sessions'][i]['min_age_limit'],new_result['sessions'][i]['available_capacity'],new_result['sessions'][i]['fee_type'],new_result['sessions'][i]['vaccine'])
		print("Total sessions : ",num1)





def loop1():
	loop2()

def loop2():
			
	GetData()
	time.sleep(32)
	loop1()


loop1()
