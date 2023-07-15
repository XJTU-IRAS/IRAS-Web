# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
# models模块尽量不要修改，如果修改一定要进行数据库迁移，具体步骤如下
# 在manage.py所在目录下
# py manage.py makemigrations
# py manage.py migrate
from django.db import models
class Experience(models.Model):# 工作经历
    name = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 名称
    info = models.TextField(db_collation='utf8mb3_bin', blank=True, null=True)
    # 具体信息
    company = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 工作地点
    time = models.IntegerField(blank=True, null=True)
    # 工作时间
    interviewee = models.ForeignKey('Interviewee', models.DO_NOTHING)
    class Meta:
        db_table = 'experience'
        
class Interviewee(models.Model):# 应聘者
    name = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    origin_text = models.TextField(db_collation='utf8mb3_bin', blank=True, null=True)
    # 原始提取文本
    age = models.IntegerField(blank=True, null=True)
    # 年龄
    work_years = models.IntegerField(blank=True, null=True)
    # 工作年限
    education = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 学历
    ideal_pos = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 求职意向
    school = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 最终毕业院校
    birth = models.DateField(blank=True, null=True)
    # 出生年月
    telephone = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    gender = models.CharField(max_length=4,db_collation='utf8mb3_bin',blank=True, null=True)
    # 性别 1为男 2为女
    native_place = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 籍贯
    political_status = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 政治面貌
    file_name = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 简历文件名称
    class Meta:
        db_table = 'interviewee'


class MatchPosition(models.Model):# 人岗匹配表，多对多
    position = models.OneToOneField('Position', models.DO_NOTHING, primary_key=True)
    # 职位
    interviewee = models.ForeignKey(Interviewee, models.DO_NOTHING)
    # 面试者
    class Meta:
        db_table = 'match_position'
        unique_together = (('position', 'interviewee'),)


class Position(models.Model):
    name = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    work_year = models.IntegerField(blank=True, null=True)
    # 最低年限要求
    education = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 最低学位要求
    file_name = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    # 岗位信息文件名称
    origin_text = models.TextField(db_collation='utf8mb3_bin', blank=True, null=True)
    # 原始提取文本
    class Meta:
        db_table = 'position'


class Project(models.Model):
    name = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    # 项目年限
    resp = models.TextField(blank=True, null=True)
    # 项目职责
    interviewee = models.ForeignKey(Interviewee, models.DO_NOTHING)
    class Meta:
        db_table = 'project'
