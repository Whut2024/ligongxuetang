import requests
from constant import login_body, header

def login():
    url = 'http://lgxt.wutp.com.cn/api/login'
    response = requests.post(url=url, data=login_body, headers=header)
    header['Authorization'] = response.json()['data']