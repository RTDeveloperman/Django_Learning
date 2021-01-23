from django.db import models
from django.utils import timezone
from Extentions.utils import jalali_converter
from django.template.defaultfilters import truncatewords  # or truncatewords

#my Managers
class ArticleManager(models.Manager):
    def published_article(self):
        return self.filter(status='p')
class CategoryManager(models.Manager):
    def active_category(self):
        return self.filter(status=True)

class Category(models.Model):
    parent=models.ForeignKey('self',default=None, null=True, blank=True, verbose_name="زیردسته",related_name='children',on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, null=False, blank=False, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=120, unique=True, null=False, blank=False, verbose_name="آدرس دسته بندی")
    status=models.BooleanField(default=True,verbose_name="آیا نمایش داده شود؟")
    position=models.IntegerField(verbose_name="پوزیشن")
    class Meta():
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering =['parent__id','position']
    def __str__(self):
        return self.title
    objects = CategoryManager()

class article(models.Model):
    STATUS_CHOICES={
        ('d','Draft'),
        ('p','Publish'),
    }
    title=models.CharField(max_length=120,null=False, blank= False,verbose_name="عنوان مقاله")
    slug=models.SlugField(max_length=120,unique=True,null=False, blank= False,verbose_name="آدرس مقاله")
    category=models.ManyToManyField(Category,verbose_name="دسته بندی",related_name='articles_rela')
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
    def category_published(self):
        return self.category.filter(status=True)
    def short_description(self):
        return truncatewords(self.description,10)
    def article_category(self):
        cate=[]
        for category in self.category.all():
            cate.append(category.title)
        return ",".join(cate)
    jpublish_time.short_description="زمان انتشار"
    objects=ArticleManager()