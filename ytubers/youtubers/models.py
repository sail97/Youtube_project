from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    crew_choices = (
        ('Solo','solo'),
        ('small_team','SM'),
        ('large_team','LM')
    )

    camera_choices = (
        ('sony','sony'),
        ('fuji','fuji'),
        ('canon','canon')
    )

    category_choices = (
        ('cooking','cook'),
        ('tech','tech'),
        ('educational','edu'),
        ('vlog','vlog')
    )

    name=models.CharField(max_length=250)
    email=models.EmailField()
    city=models.CharField(max_length=200)
    desc=RichTextField()
    video_url=models.CharField(max_length=500)
    price=models.CharField(max_length=10)
    height=models.IntegerField()
    subs_count=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    crew=models.CharField(choices=crew_choices,max_length=100)
    camera_type=models.CharField(choices=camera_choices,max_length=100)
    category=models.CharField(choices=category_choices,max_length=100)
    photo=models.ImageField(upload_to='media/youtubers/%Y/%M/%D')
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name