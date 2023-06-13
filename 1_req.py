import requests

url = "https://courses.wscubetech.com"
r = requests.get(url)
print(r.status_code)
print(r.text)