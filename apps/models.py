from django.db import models

# Create your models here.


class MyUser(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "my_user_table"