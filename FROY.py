import requests, json

response = requests.get('http://ipinfo.io/json')
x = json.loads(response.text)['country']
if 'NG 'in str(x):
  print("Enter the script")
else:
  print(x)

P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("FROY").Checkin_()
	else:
		__import__("FROY").Checkin_()

