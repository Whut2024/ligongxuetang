import requests
from constant import header

def get_eligible_books_id() -> list:
    url = 'http://lgxt.wutp.com.cn/api/myCourses'
    response = requests.post(url=url, headers=header)
    course_id_list = list()
    course_list = response.json()['data']
    print(response.text)
    for course in course_list:
        course_id_list.append(course['courseId'])
    return course_id_list