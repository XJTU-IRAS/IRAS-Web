from django.db import connection
from django.test import TestCase
# Create your tests here.
import tempfile
import models
cursor = connection.cursor()
SQL1='''SELECT COUNT(*) AS count,
 CASE 
 WHEN education = '大专'  THEN '专科' 
 WHEN education = '本科' OR education = '学士'  THEN '本科' 
 WHEN education = '研究生' OR education = '硕士'  THEN '硕士' 
 WHEN education = '博士'   THEN '博士' 
 WHEN education = '小学' OR education = '中专' OR education = '初中' OR education = '高中' THEN '高中及以下' 
 ELSE '未知'
 END AS education_group FROM interviewee WHERE id>={start} AND id<={end} GROUP BY education_group;'''.format(start=start, end=end)
cursor.execute(SQL1)
result = cursor.fetchall()
print(result)