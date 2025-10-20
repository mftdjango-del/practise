from django.db import models

# Create your models here.

class ProductModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    text = models.TextField(null=True, verbose_name="توضیحات")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    uuid = models.CharField(max_length=50, null=True, blank=True, verbose_name="شناسه")
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, null=True, blank=True, verbose_name="عنوان در مرورگر")
    count = models.IntegerField(default=0, verbose_name="تعداد موجودی")
    auction = models.BooleanField(default=False, verbose_name="حراج")

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = self.title.strip().replace(' ', '-')
        return super().save(*args,**kwargs)
    def is_new_product(self):
        new_products = ProductModel.objects.filter(is_active=True).order_by("-id")[:2]
        if self in new_products:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        