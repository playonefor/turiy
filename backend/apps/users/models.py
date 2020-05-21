from django.db import models
from django.contrib.auth.models import AbstractUser, Group

'''
# 自定义模型
class tManager(models.Manager):
    pass
'''


class tGroup(Group):
    comment = models.TextField(blank=True)

    class Meta:
        verbose_name = "用户组"
        verbose_name_plural = verbose_name
        ordering = ('name',)


class UserProfile(AbstractUser):

    """用户信息"""
    password = models.CharField(
        "密码",
        max_length=100,
        null=True,
        blank=True
    )
    name = models.CharField(
        "姓名",
        max_length=20,
        null=True,
        blank=True
    )
    tgroup = models.ManyToManyField(
        tGroup,
        related_name='users',
        verbose_name="用户组"
    )
    mobile = models.CharField(
        "手机号",
        max_length=11,
        null=True,
        blank=True,
        help_text="手机号"
    )
    email = models.EmailField(
        "邮箱",
        max_length=100,
        null=True,
        blank=True,
    )
    wechat = models.CharField(
        "微信",
        max_length=100,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
