from django.db import models
from django.utils import timezone
from Extentions.utils import jalali_converter
from django.template.defaultfilters import truncatewords  # or truncatewords


class Category(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=120, unique=True, null=False, blank=False, verbose_name="آدرس دسته بندی")
    status=models.BooleanField(default=True,verbose_name="آیا نمایش داده شود؟")
    position=models.IntegerField(verbose_name="پوزیشن")
    class Meta():
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering =['position']
    def __str__(self):
        return self.title


class article(models.Model):
    STATUS_CHOICES={
        ('d','Draft'),
        ('p','Publish'),
    }
    title=models.CharField(max_length=120,null=False, blank= False,verbose_name="عنوان مقاله")
    slug=models.SlugField(max_length=120,unique=True,null=False, blank= False,verbose_name="آدرس مقاله")
    category=models.ManyToManyField(Category,verbose_name="دسته بندی")
    description=models.TextField(verbose_name="متن مقاله")
    thumbnail=models.ImageField(upload_to="images",verbose_name="تصویر مقاله")
    publish_time=models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created=models.DateTimeField(auto_now_add=True,verbose_name="")
    updated=models.DateTimeField(auto_now=True,verbose_name="")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت انتشار")
    class Meta():
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
        ordering =['-publish_time']

    def __str__(self):
        return self.title
    def jpublish_time(self):
        return jalali_converter(self.publish_time)
    def short_description(self):
        return truncatewords(self.description,10)
    jpublish_time.short_description="زمان انتشار"