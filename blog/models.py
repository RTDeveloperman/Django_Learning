from django.db import models
from django.utils import timezone
from Extentions.utils import jalali_converter
class article(models.Model):
    STATUS_CHOICES={
        ('d','Draft'),
        ('p','Publish'),
    }
    title=models.CharField(max_length=120,null=False, blank= False,verbose_name="عنوان مقاله")
    slug=models.SlugField(max_length=120,unique=True,null=False, blank= False,verbose_name="آدرس مقاله")
    description=models.TextField(verbose_name="متن مقاله")
    thumbnail=models.ImageField(upload_to="images",verbose_name="تصویر مقاله")
    publish_time=models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created=models.DateTimeField(auto_now_add=True,verbose_name="")
    updated=models.DateTimeField(auto_now=True,verbose_name="")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت انتشار")
    class Meta():
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
    def __str__(self):
        return self.title
    def jpublish_time(self):
        return jalali_converter(self.publish_time)
    jpublish_time.short_description="زمان انتشار"