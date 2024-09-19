import time

import requests
from constant import header

def set_full_marks(work_id_list: list):
    
    full_marks_body = {
        'grade': 100,
        'workId': ''
    }
    
    url = 'http://lgxt.wutp.com.cn/api/submitAnswer'
    
    for work_id in work_id_list:
        full_marks_body['workId'] = work_id
        response = requests.post(url=url, data=full_marks_body, headers=header)
        print(response.text)
        time.sleep(0.3)