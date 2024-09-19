import requests
from constant import header


def get_work_id(course_id_list: list) -> list:
    url = 'http://lgxt.wutp.com.cn/api/myCourseWorks'

    work_body = {
        'courseId': ''
    }

    work_id_list = []

    for course_id in course_id_list:
        work_body['courseId'] = course_id
        response = requests.post(url=url, headers=header, data=work_body)

        if response.json()['code'] != 0:
            continue

        print(response.text)

        work_list = response.json()['data']
        for work in work_list:
            work_id_list.append(work['workId'])

    return work_id_list
