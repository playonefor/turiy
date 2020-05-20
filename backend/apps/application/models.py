from django.db import models


class Application(models.Model):
    ENV = (
        (0, '开发环境'),
        (1, '测试环境'),
        (2, 'beta环境'),
        (3, '生产环境'),
    )
    name = models.CharField(
        '应用名称',
        max_length=100,
        unique=True
    )
    env = models.CharField(
        '环境',
        max_length=20,
        choices=ENV
    )
    comment = models.CharField(
        '备注',
        max_length=1000
    )

    class Meta:
        verbose_name = '应用'
        verbose_name_plural = verbose_name
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)
