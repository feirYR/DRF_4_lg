from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    age=models.SmallIntegerField()
    class Meta:
        db_table='user_login'
        verbose_name='用户'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username