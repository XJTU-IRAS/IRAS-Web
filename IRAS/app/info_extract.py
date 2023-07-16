import docx2txt
from pprint import pprint
import re
from paddlenlp import Taskflow
import json
import os
from tqdm import tqdm


#DOCX_PATH = r'D:\OneDrive\桌面\resume_analyze\data'
#JSON_PATH = './json/full_info_dict.json'
#MODEL = r'D:\OneDrive\桌面\resume_analyze\model\UIE'

# 简历基本信息
base_schema = ['姓名', '生日', '年龄', '性别', '求职意向']
base_schema_en = { '姓名': 'name', '年龄': 'age', '性别': 'sex', '求职意向': 'job_intention' }

'''
def get_text(file_path):
    # 读取docx文件并去除空格和制表符
    row_text = docx2txt.process(file_path).replace(' ', '').replace('\t', '')
    # 将多个换行符替换为一个换行符
    row_text = re.sub(r'\n+', '\n', row_text).split('\n')
    # 按照换行符分割并去重
    seen = set()
    text_list = []
    for row in row_text:
        if row not in seen:
            text_list.append(row.strip())
            seen.add(row)
    text = '\n'.join(text_list)

    return text
'''



def get_edu_info(text_list, begin, end, ie):
    edu_dict = { -1: '无', 0: '小学', 1: '初中', 2: '中专', 3: '高中', 4: '大专', 5: '本科', 6: '硕士', 7: '博士' }
    ie.set_schema(['学校'])
    max_edu = -1
    flag = -1
    index = []
    college = []
    for i in range(begin, end):
        if '小学' in text_list[i]:
            flag = 0
        if '初中' in text_list[i]:
            flag = 1
        if '中专' in text_list[i] or '学校' in text_list[i]:
            flag = 2
        if '高中' in text_list[i] or '中学' in text_list[i] or '一中' in text_list[i]:
            flag = 3
        if '学院' in text_list[i]:
            flag = 5
            college.append(i)
        if '技术学院' in text_list[i] or '职业学院' in text_list[i]:
            flag = 4
            college.remove(i)
        if '大学' in text_list[i] and '附属中学' not in text_list[i] and '大学英语' not in text_list[
            i] and '大学生' not in text_list[i]:
            flag = 5
            college.append(i)
        if '学士' in text_list[i] or '本科' in text_list[i]:
            flag = 5
        if '硕士' in text_list[i]:
            flag = 6
        if '博士' in text_list[i]:
            flag = 7
        if max_edu == flag and max_edu != -1:
            index.append(i)
        if max_edu < flag:
            max_edu = flag
            index = [i]
        flag = -1

    school = ''
    # 如果最高学历是硕士或博士
    if max_edu == 6 or max_edu == 7:
        last = index[-1]
        for i in college:
            if i <= last:
                school_info = ie(text_list[i])
                pprint(school_info)
                # 提取学校
                if '学校' in school_info[0].keys():
                    school = school_info[0]['学校'][0]['text']
                    break
        if school == '':
            for i in college:
                if i > last:
                    school_info = ie(text_list[i])
                    pprint(school_info)
                    # 提取学校
                    if '学校' in school_info[0].keys():
                        school = school_info[0]['学校'][0]['text']
                        break
    # 如果最高学历是本科
    if max_edu == 5:
        for i in college:
            school_info = ie(text_list[i])
            pprint(school_info)
            # 提取学校
            if '学校' in school_info[0].keys():
                school = school_info[0]['学校'][0]['text']
                break
    if max_edu != -1 and max_edu < 5:
        for i in index:
            print('教育' + text_list[i])
            school_info = ie(text_list[i])
            pprint(school_info)
            # 提取学校
            if '学校' in school_info[0].keys():
                school = school_info[0]['学校'][0]['text']
                break
    return edu_dict[max_edu], school


def get_work_info(text_list, begin, end, ie):
    cls = Taskflow("zero_shot_text_classification",
                   schema = ['是工作经历', '是教育经历', '不是工作经历'])
    years = 0
    predict_years = 0
    work_experience = []
    pre_date_list = []
    section = ''
    for line in text_list[begin:end]:
        is_work_experience = False
        # 统计line中数字的个数huoqu
        date_list = re.findall(r'(\d+)', line)
        num = len(date_list)
        if 3 <= num <= 4 or '至今' in line:
            if len(line) <= 18:
                line = line + text_list[
                    text_list.index(line) + 1 if text_list.index(line) + 1 < len(text_list) else text_list.index(line)]
            print(line)
            cls_info = cls(line)
            pprint(cls_info)
            if '至今' in line:
                if len(cls_info[0]['predictions']) > 0 and cls_info[0]['predictions'][0]['label'] == '是工作经历':
                    is_work_experience = True
                    # 计算工作年限
                    if num == 2:
                        years += calculate_years(int(date_list[0]), int(date_list[1]), 2023, 4)
                        section = date_list[0] + '.' + date_list[1] + '至今'
                    elif num == 1:
                        years += calculate_years(int(date_list[0]), 1, 2023, 4)
                        section = date_list[0] + '至今'
                    elif num >2 and len(date_list[-2]) == 4:
                        years += calculate_years(int(date_list[-2]), int(date_list[-1]), 2023, 4)
                        section = date_list[-2] + '.' + date_list[-1] + '至今'
                    elif len(pre_date_list) == 2:
                        years += calculate_years(int(pre_date_list[0]), int(pre_date_list[1]), 2023, 4)
                        section = pre_date_list[0] + '.' + pre_date_list[1] + '至今'
                elif len(pre_date_list) == 2:
                    predict_years += calculate_years(int(pre_date_list[0]), int(pre_date_list[1]), 2023, 4)
            elif num == 4:
                if len(cls_info[0]['predictions']) > 0 and cls_info[0]['predictions'][0]['label'] == '是工作经历':
                    is_work_experience = True
                    years += calculate_years(int(date_list[0]), int(date_list[1]), int(date_list[2]), int(date_list[3]))
                    section = date_list[0] + '.' + date_list[1] + '-' + date_list[2] + '.' + date_list[3]
                elif len(cls_info[0]['predictions']) == 0:
                    predict_years += calculate_years(int(date_list[0]), int(date_list[1]), int(date_list[2]),
                                                     int(date_list[3]))
            elif num == 3:
                if len(cls_info[0]['predictions']) > 0 and cls_info[0]['predictions'][0]['label'] == '是工作经历':
                    is_work_experience = True
                    years += calculate_years(int(date_list[0]), int(date_list[1]), int(date_list[0]), int(date_list[2]))
                    section = date_list[0] + '.' + date_list[1] + '-' + date_list[0] + '.' + date_list[2]
                elif len(cls_info[0]['predictions']) == 0:
                    predict_years += calculate_years(int(date_list[0]), int(date_list[1]), int(date_list[0]),
                                                     int(date_list[2]))

            # 提取公司名称
            if is_work_experience:
                ie.set_schema(['公司', '职位'])
                work_info = ie(line)
                if '公司' in work_info[0].keys():
                    company = work_info[0]['公司'][0]['text']
                else:
                    company = ''
                if '职位' in work_info[0].keys():
                    job = work_info[0]['职位'][0]['text']
                else:
                    job = ''
                work_experience.append({ 'section': section, 'company': company, 'job': job })
        print(years, predict_years)
        pre_date_list = date_list
    if years == 0:
        years = predict_years
    if years > 100 or years < 0:
        years = 0
    return years, work_experience


def replace_keys(dictionary, replacements):
    new_dict = { }
    for key, value in dictionary.items():
        if key in replacements:
            new_key = replacements[key]
        else:
            new_key = key
        new_dict[new_key] = value
    return new_dict


def info_extract(text):
    
    info = { }
    module_index = { }
    print(text)
    text_list = text.split('\n')
    # 实体提取
    ie = Taskflow("information_extraction", schema = base_schema)
    base_info = ie(text)
    pprint(base_info)
    # 将实体写入字典
    for item in base_info:
        for field, values in item.items():
            probability = 0
            text = ''
            for value in values:
                if value['probability'] > probability:
                    probability = value['probability']
                    text = value['text']
            if probability > 0.33:
                if field == '年龄' and len(text) > 3:
                    continue
                if field == '性别' and probability < 0.9:
                    continue
                info[field] = text.replace('岁', '')

    # 提取年龄
    if '生日' in info.keys():
        # 正则匹配岁数
        birthday = re.findall(r'(\d{4})', info['生日'])
        if len(birthday) > 0:
            # 计算岁数
            age = 2023 - int(birthday[0]) + 1
            if '年龄' not in info.keys():
                info['年龄'] = str(age)
        info.pop('生日')
    else:
        if '年龄' not in info.keys():
            # 正则匹配年龄
            age = re.findall(r'(\d{2})岁', text)
            if len(age) > 0:
                info['年龄'] = age[0].replace('岁', '')

    info = replace_keys(info, base_schema_en)

    # 划分模块
    for line in text_list:
        # 判断教育模块起始位置
        if '教育' in line and len(line) < 12:
            module_index['教育'] = text_list.index(line)
        # 判断工作模块起始位置
        if '工作经历' in line or '工作经验' in line or '工作背景' in line:
            module_index['工作'] = text_list.index(line)
        # 判断项目模块起始位置
        if '项目' in line and len(line) < 12:
            module_index['项目'] = text_list.index(line)
        # 判断证书模块起始位置
        if '证书' in line and len(line) < 12:
            module_index['证书'] = text_list.index(line)
        # 判断技能模块起始位置
        if '技能' in line and len(line) < 12:
            module_index['技能'] = text_list.index(line)
        # 判断荣誉或奖项模块起始位置
        if ('荣誉' or '奖') in line and len(line) < 12:
            module_index['荣誉'] = text_list.index(line)
        # 判断自我评价模块起始位置
        if '自我评价' in line and len(line) < 12:
            module_index['自我评价'] = text_list.index(line)
    # 根据模块起始位置排序
    values = sorted([value for value in module_index.values()])
    print(values)

    # 提取教育信息
    if '教育' in module_index.keys():
        edu, school = get_edu_info(text_list, module_index['教育'], len(text_list), ie)
        if edu == '无' or school == '':
            edu, school = get_edu_info(text_list, 0, module_index['教育'], ie)
        info['education'] = edu
        info['school'] = school

    else:
        edu, school = get_edu_info(text_list, 0, len(text_list), ie)
        info['education'] = edu
        info['school'] = school

    years = 0
    # 提取工作信息
    if '工作' in module_index.keys():
        begin = module_index['工作']
        index = values.index(begin)
        end = values[index + 1] if index < len(values) - 1 else len(text_list)
        years, work_experience = get_work_info(text_list, begin, end, ie)
        # 工作年限为0则提取全文
        if years == 0:
            years, work_experience = get_work_info(text_list, 0, len(text_list), ie)
        info['work_time'] = str(years)
        info['work_experience'] = work_experience
    else:
        info['work_time'] = str(0)
    # 转为英文键值
    return info


def calculate_years(start_year, start_month, end_year, end_month):
    # 计算相差月数
    month = (end_year - start_year) * 12 + (end_month - start_month)
    # 计算相差年数
    year = month // 12
    # 有余数则年数加1
    if month % 12 != 0:
        year += 1
    return year


