import requests

# POST 요청 보내기

# 요청을 보낼 URL
URL = "URL"

# 헤더 추가
headers = {
    'Authorization': 'Bearer your_token_here',
    'Content-Type': 'application/json',
    'User-Agent': 'your_user_agent',
    'Accept': 'application/json'
}
# requests.post() options
# 1. url : 요청을 보낼 url
# 2. data : URL에 추가할 쿼리 문자열, 딕셔너리 형태로 전달
# 3. json : JSON 형식의 데이터를 서버에 전송할 때 사용, Content-Type 헤더가 자동으로 application/json으로 설정됨
#    (ex) response = requests.post(url, json=json_data)
# 3. headers : 요청에 포함할 HTTP 헤더, 딕셔너리 형태로 전달
# 4. cookies : 요청에 포함할 쿠키, 딕셔너리 형터래 전달
# 5. auth : 인증 정보를 제공하기 위해사용 : 이건 잘 모르겠음...
# 6. timeout : 요청에 대한 대기 시간을 설정, 이 시간내에 요청이 완료되지 않으면 Timeout 예외 발생
# 7. allow_redirects : 리다이렉트를 허용할지 여부를 설정, 기본값 : True(서버가 3XX 상태코드를 반환하면 클라이언트는 자동으로 리디렉션을 따름)
# 8. stream : 응답 본문을 즉시 다운로드할지 여부를 설정
# 9. verify : SSL 인증서를 검증할지 여부를 설정, 기본값 : True(False로 하면 SSL 인증서 검증을 생략함)
# 10. proxies : 요청에 사용할 프록시 서버, 딕셔너리 형태로 전달

# body에 data 추가
data = {
    'data1' : 'example1',
    'data2' : 'example2'
}   

response = requests.get(URL, data=data)