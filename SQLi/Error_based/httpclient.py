import http.client
import json

conn = http.client.HTTPConnection("www.google.com")

# GET 요청 보내기
headers = {
    "User-Agent": "MyCustomUserAgent/1.0",
    "Accept": "text/html",
    "Authorization": "Bearer your_token"
}

conn.request("GET", "/", headers=headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data.decode())


# POST 요청 보내기
headers = {
    "Content-Type": "application/json",
    "User-Agent": "MyCustomUserAgent/1.0"
}

payload = json.dumps({"key1": "value1", "key2": "value2"})

conn.request("POST", "/api/endpoint", body=payload, headers=headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data.decode())