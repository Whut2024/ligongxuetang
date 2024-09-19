import time

from login import login
from get_eligible_books import get_eligible_books_id
from get_work_id import get_work_id
from set_full_marks import set_full_marks

login()
time.sleep(0.5)
course_id_list = get_eligible_books_id()
time.sleep(0.5)
work_id_list = get_work_id(course_id_list)
time.sleep(0.5)
set_full_marks(work_id_list)