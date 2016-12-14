from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#仪器模型
class Instruments(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


#预约情况
class Order(models.Model):
    user = models.ForeignKey(User, default=1)
    instrument = models.ForeignKey(Instruments, default=1)
    time = models.DateField()

    def __str__(self):
        return str(self.user) + '-' + str(self.instrument)