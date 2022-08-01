from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    def myPhoto(self,object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))

    list_display=('id','myPhoto','name','category','is_featured')
    list_filter= ('category' , 'camera_type' , 'crew')
    list_editable=('is_featured',)
    search_fields = ('name' , 'city' , 'camera_type' , 'category')


admin.site.register(Youtuber,YoutuberAdmin)