import requests
import json
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date=31-03-2021'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
result = requests.get(url, headers=headers)

#print(result.json())
new_result=result.json()

num=len(new_result['sessions'])
num1=num

for i in range(num):
	print(i+1,new_result['sessions'][i]['center_id'],new_result['sessions'][i]['name'])


    

print("Total Sessions : ",num1)

#print(new_result['sessions'][0]['center_id'])
#print(new_result['sessions'][0]['name'])
