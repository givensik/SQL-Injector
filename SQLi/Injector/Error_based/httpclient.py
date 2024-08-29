import http.client
import json
import urllib.parse

conn = http.client.HTTPConnection("host3.dreamhack.games", 22222)

# GET 요청 보내기
headers = {

}

# 쿼리 문자열 생성
params = {
    'uid': 'test',
}
query_string = urllib.parse.urlencode(params)

# GET 요청 보내기 (쿼리 문자열을 URL에 추가)
conn.request("GET", f"/?{query_string}")

# conn.request("GET", "/", headers=headers)

response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data.decode())


# # POST 요청 보내기
# headers = {
#     "Content-Type": "application/json",
#     "User-Agent": "MyCustomUserAgent/1.0"
# }

# payload = json.dumps({"key1": "value1", "key2": "value2"})

# conn.request("POST", "/api/endpoint", body=payload, headers=headers)
# response = conn.getresponse()
# print(response.status, response.reason)
# data = response.read()
# print(data.decode())