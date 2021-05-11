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

dataB1=np.array([])
data1 = 0

def GetData():
	global dataB1
	global data1
	for x in range(7):
		Date=Week[x].strftime('%d-%m-%Y')
		
		url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date={}'.format(Date)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
		result = requests.get(url, headers=headers)
		new_result=result.json()
		num=len(new_result['sessions'])
		# print("\n"new_result['sessions'][0]['name'])
		modifiedlist = [""]
		if num>0:
			print('\n')
			print("Date : ",Date)
		num1=num
		for i in range(num):
			# print(i+1,new_result['sessions'][i]['center_id'],new_result['sessions'][i]['name'],new_result['sessions'][i]['min_age_limit'],new_result['sessions'][i]['available_capacity'],new_result['sessions'][i]['fee_type'],new_result['sessions'][i]['vaccine'])
			modifiedlist.append(i+1)
			modifiedlist.append(new_result['sessions'][i]['center_id'])
			modifiedlist.append(new_result['sessions'][i]['name'])
			modifiedlist.append(new_result['sessions'][i]['min_age_limit'])
			modifiedlist.append(new_result['sessions'][i]['available_capacity'])
			modifiedlist.append(new_result['sessions'][i]['fee_type'])
			modifiedlist.append(new_result['sessions'][i]['vaccine'])
			dataB1=np.insert(dataB1,i,i+1)
		print(modifiedlist)

	NOA=len(dataB1)
	print("\nDataBase:",dataB1)
	print("Total Sessions : ",NOA)
	for i in range(NOA-1,-1,-1):
		dataB1=np.delete(dataB1,i)
	print(dataB1)
	print(len(dataB1))
	

	if NOA!=data1:
		print("Update available")
		data1=NOA

def loop1():
	loop2()

def loop2():
			
	GetData()
	time.sleep(64)#32
	loop1()


#loop1()
GetData()



