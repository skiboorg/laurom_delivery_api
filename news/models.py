from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField



class NewsItem(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    image = ResizedImageField('Картинка превью',size=[470, 315], quality=95, force_format='WEBP', upload_to='news/images',
                              blank=False, null=True)
    image_top = ResizedImageField('Картинка вверху статьи (1080x450)', size=[1080, 450], quality=95, force_format='WEBP',
                              upload_to='news/images',
                              blank=False, null=True)

    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ',max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    description = models.TextField('Короткое описание', blank=True, null=True)

    content_editor = RichTextUploadingField('Редактор', blank=True, null=True)
    content = models.TextField('Контент', blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Image(models.Model):
    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE, related_name='images')
    image = models.FileField('Картинка', upload_to='news/images', blank=False, null=True)