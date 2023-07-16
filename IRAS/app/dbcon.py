from django.db import connection
def education_group(start,end):
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
    return result
def year_group(start,end):
    cursor = connection.cursor()
    SQL2='''SELECT COUNT(*) AS count,
 CASE 
 WHEN age < 18 THEN '0-18' 
 WHEN age >= 18 AND age <=22  THEN '18-22' 
 WHEN age >= 23 AND age <=27 THEN '23-27' 
 WHEN age >=28 AND age <=32 THEN '28-32'
 WHEN age >=33 AND age <=37 THEN '33-37'
 WHEN age >=38 AND age <=45 THEN '38-45'
 WHEN age >=46 AND age <=50 THEN '46-50'
 WHEN age >50 THEN '50以上'
 ELSE '未知'
 END AS age_group FROM interviewee WHERE id>={start} AND id<={end} GROUP BY age_group;
'''.format(start=start, end=end)
    cursor.execute(SQL2)
    result = cursor.fetchall()