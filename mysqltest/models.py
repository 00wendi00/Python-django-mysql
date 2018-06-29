from django.db import models

# Create your models here.

__author__ = 'wade cheung'


class UserInfo(models.Model):
    class Meta:
        db_table = 'user_test'

    id = models.AutoField(max_length=12, db_column='id', primary_key=True)
    user = models.CharField(max_length=32, db_column='user', blank=True)
    pwd = models.CharField(max_length=32, db_column='password', blank=True)


class Charactor(models.Model):
    class Meta:
        db_table = 'user_charactor'

    cid = models.AutoField(max_length=11, db_column='CID', primary_key=True)
    charactor = models.CharField(max_length=255, db_column='charactor', blank=False)
    hGroup = models.IntegerField(max_length=11, db_column='h_group', blank=False)
