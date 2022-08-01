

# Create your models here.

from datetime import datetime
from django.db import models
from datetime import datetime

# Create your models here.

class Hiretuber(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    tuber_id=models.IntegerField()
    user_id=models.IntegerField()
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=250)
    tuber_name=models.CharField(max_length=250)
    phone=models.CharField(max_length=100)
    message=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)

def __str__(self):
    return self.email