from django.db import models

# Create your models here.

__author__ = 'wade cheung'


class UserInfo(models.Model):
    class Meta:
        db_table = 'user_test'
        app_label = 'oracletest'

    id = models.AutoField(max_length=12, db_column='id', primary_key=True)
    user = models.CharField(max_length=32, db_column='user', blank=True)
    pwd = models.CharField(max_length=32, db_column='password', blank=True)
