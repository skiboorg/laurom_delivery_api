
from pytils.translit import slugify

from django.db import models
from django_resized import ResizedImageField

from ckeditor_uploader.fields import RichTextUploadingField


class Feature(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    icon = ResizedImageField(size=[100, 100], quality=95, force_format='WEBP', upload_to='service/icon',
                             blank=True, null=True)
    description = models.TextField('Короткое описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Преимущества услуги'
        verbose_name_plural = 'Преимущества услуги'

class Step(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    number = models.CharField(max_length=255, blank=True, null=False)
    description = models.TextField('Короткое описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Этапы услуги'
        verbose_name_plural = 'Этапы услуги'

class Price(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    price = models.CharField(max_length=255, blank=True, null=False)
    description = models.TextField('Короткое описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'

class Faq(models.Model):
    q = models.CharField('Вопрос', max_length=255, blank=False, null=False)
    a = models.CharField('Ответ',max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.q} - {self.a}'

    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faq'

class Category(models.Model):
    order_num = models.IntegerField('Номер П/П', default=1, blank=False, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField('Короткое описание', blank=True, null=True)
    html_content = RichTextUploadingField(verbose_name='Редактор', blank=True, null=True)
    content = models.TextField('СЕО Контент', blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.name_slug:
            self.name_slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    order_num = models.IntegerField('Номер П/П', default=1, blank=False, null=True)
    is_active = models.BooleanField('Отображать?', default=True)
    category = models.ManyToManyField(Category, verbose_name='Категория', blank=False, related_name='services')

    name = models.CharField('Название', max_length=255, blank=False, null=False)
    name_slug = models.CharField('ЧПУ',max_length=255,blank=True, null=True)
    icon = ResizedImageField(size=[100, 100], quality=95, force_format='WEBP', upload_to='service/icon',
                              blank=True, null=True)
    image_top = ResizedImageField(size=[1920, 700], quality=95, force_format='WEBP', upload_to='service/icon',
                             blank=True, null=True)
    image_middle = ResizedImageField(size=[1920, 550], quality=95, force_format='WEBP', upload_to='service/icon',
                              blank=True, null=True)

    description = models.TextField('Короткое описание', blank=True, null=True)
    about_us = models.TextField('О нас', blank=True, null=True)
    features = models.ManyToManyField(Feature, blank=True)
    steps = models.ManyToManyField(Step, blank=True)
    prices = models.ManyToManyField(Price, blank=True)
    faqs = models.ManyToManyField(Faq, blank=True)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        self.name_slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    def __str__(self):
        return f'{self.name}'

class Case(models.Model):
    order_num = models.IntegerField('Номер П/П', default=1, blank=False, null=True)
    date = models.CharField('Дата', max_length=10, blank=False, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    name_slug = models.CharField('ЧПУ', max_length=255, blank=True, null=True)
    image = ResizedImageField(size=[590, 330], quality=95, force_format='WEBP', upload_to='case/gallery',
                              blank=False, null=True)
    description = models.TextField('Короткое описание', blank=False, null=True)
    html_content = RichTextUploadingField(verbose_name='Редактор', blank=True, null=True)
    content = models.TextField('СЕО текст', blank=True, null=True)
    services = models.ManyToManyField(Service,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        self.name_slug = slugify(self.name)
        super().save(*args, **kwargs)

class CaseGalleryImage(models.Model):
    order_num = models.IntegerField('Номер П/П', default=1, blank=False,null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='images')
    image = models.FileField( upload_to='case/gallery',blank=False, null=True)
    is_main = models.BooleanField('Основная картинка', default=False)

    def __str__(self):
        return f''


    class Meta:
        ordering = ('-is_main', 'order_num')
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки кейсов'


