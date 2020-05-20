from django.db import models
from django.contrib.auth import get_user_model
from application.models import Application
from users.models import tGroup

# Create your models here.
User = get_user_model()


class PerMisson(models.Model):
    name = models.CharField(
        '权限名称',
        max_length=100,
        unique=True
    )
    app = models.ManyToManyField(
        Application,
        blank=True,
        verbose_name='应用'
    )
    users = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='用户'
    )
    group = models.ManyToManyField(
        tGroup,
        blank=True,
        verbose_name='用户组'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    content = models.CharField(
        '备注',
        max_length=1000
    )

    class Meta:
        unique_together = [('name',)]
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)
