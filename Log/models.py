from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=50, verbose_name='密码')
    email = models.EmailField(default='', verbose_name='用户邮箱')
    #icon = models.ImageField()
    confirmed = models.BooleanField(default=False, verbose_name='是否点击邮件确认')
    location = models.CharField(max_length=100, default='', verbose_name='用户所在地')
    about_me = models.TextField(default='', verbose_name='用户的自我描述')

    class Meta:
        db_table = 'Users'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name