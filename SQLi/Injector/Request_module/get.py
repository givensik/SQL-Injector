import requests

# GET 요청 보내기

# 요청을 보낼 URL
URL = "URL"

# 헤더 추가
headers = {
    'Authorization': 'Bearer your_token_here',
    'Content-Type': 'application/json',
    'User-Agent': 'your_user_agent',
    'Accept': 'application/json'
}
# requests.get() options
# 1. url : 요청을 보낼 url
# 2. params : URL에 추가할 쿼리 문자열, 딕셔너리 형태로 전달
# 3. headers : 요청에 포함할 HTTP 헤더, 딕셔너리 형태로 전달
# 4. cookies : 요청에 포함할 쿠키, 딕셔너리 형터래 전달
# 5. auth : 인증 정보를 제공하기 위해사용 : 이건 잘 모르겠음...
# 6. timeout : 요청에 대한 대기 시간을 설정, 이 시간내에 요청이 완료되지 않으면 Timeout 예외 발생
# 7. allow_redirects : 리다이렉트를 허용할지 여부를 설정, 기본값 : True(서버가 3XX 상태코드를 반환하면 클라이언트는 자동으로 리디렉션을 따름)
# 8. stream : 응답 본문을 즉시 다운로드할지 여부를 설정
# 9. verify : SSL 인증서를 검증할지 여부를 설정, 기본값 : True(False로 하면 SSL 인증서 검증을 생략함)
# 10. proxies : 요청에 사용할 프록시 서버, 딕셔너리 형태로 전달

# 파라미터 추가
params = {
    'query1' : 'example1',
    'query2' : 'example2'
}   

response = requests.get(URL, params=params)


# 응답 출력

# 상태코드 
# 1. 1xx(정보)
# 100 Continue: 클라이언트가 요청을 계속 진행해도 좋다는 의미입니다.
# 101 Switching Protocols: 클라이언트가 요청한 프로토콜로 전환할 때 사용됩니다.

# 2. 2xx(성공)
# 200 OK: 요청이 성공적으로 처리되었음을 나타냅니다.
# 201 Created: 요청이 성공적으로 처리되어 새로운 리소스가 생성되었음을 나타냅니다.
# 204 No Content: 요청은 성공했지만 응답할 콘텐츠가 없음을 의미합니다.

# 3. 3xx(리다이렉션)
# 301 Moved Permanently: 요청한 리소스가 영구적으로 다른 URL로 이동했음을 나타냅니다.
# 302 Found: 요청한 리소스가 임시로 다른 URL로 이동했음을 나타냅니다.
# 304 Not Modified: 클라이언트가 캐시한 버전이 최신임을 의미하며, 서버에서 수정된 내용이 없음을 나타냅니다.

# 4. 4xx(클라이언트 오류)
# 400 Bad Request: 잘못된 요청을 의미합니다. 서버가 요청을 이해하지 못했습니다.
# 401 Unauthorized: 인증이 필요하거나 인증 정보가 잘못되었음을 의미합니다.
# 403 Forbidden: 서버가 요청을 거부했음을 의미합니다. 권한이 없다는 뜻입니다.
# 404 Not Found: 요청한 리소스를 찾을 수 없음을 의미합니다.**

# 5. 5xx(서버 오류)
# 500 Internal Server Error: 서버에서 예기치 않은 오류가 발생했음을 의미합니다.
# 502 Bad Gateway: 게이트웨이나 프록시 서버가 잘못된 응답을 받았음을 의미합니다.
# 503 Service Unavailable: 서버가 과부하 상태이거나 유지보수 중임을 의미합니다.

print("상태 코드:", response.status_code)
print("응답 본문:", response.text)
print("JSON 데이터:", response.json())
print("응답 헤더:", response.headers)
print("응답 URL:", response.url)
print("응답 시간:", response.elapsed)
print("최종 URL:", response.history)

