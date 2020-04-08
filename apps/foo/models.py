from django.db import models

# Create your models here.


class VisitLogModel(models.Model):
    """
    """
    visit_at = models.DateTimeField('访问时间', auto_now_add=True)
    http_url = models.CharField('路径', max_length=256)
