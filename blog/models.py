from django.urls import reverse
from django.db import models


class Person(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=40)
    first_name = models.CharField(verbose_name='Имя', null=True, max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', null=True, max_length=45)
    profile_pic = models.ImageField(verbose_name='Аватарка', null=True, blank=True, upload_to='image/')
    email_addres = models.EmailField(verbose_name='Email адрес', null=True, blank=True)
    link_github = models.URLField(verbose_name='Ссылка на Гитхаб', null=True, blank=True)
    link_linkedin = models.URLField(verbose_name='Ссылка на Linkedin', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автора'
        verbose_name_plural = 'Автор'


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=35)
    slug = models.SlugField(verbose_name='URL', max_length=35, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tags(models.Model):
    title = models.CharField(verbose_name='Название тега', max_length=35)
    slug = models.SlugField(verbose_name='URL', unique=True, max_length=35)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Works(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='works')
    title = models.CharField(verbose_name='Название проекта', max_length=40)
    slug = models.SlugField(verbose_name='URL', max_length=40, unique=True)
    views = models.IntegerField(verbose_name='Кол-во просмотров', default=0)
    work_preview = models.ImageField(verbose_name='Превью работы', null=True, blank=True, upload_to='image/works/')
    description = models.TextField(verbose_name='Описание проекта', blank=True)
    link_source_code = models.URLField(verbose_name='Ссылка на исходный код проекта', blank=True)
    link_webpage = models.URLField(verbose_name='Ссылка на страницу проекта', blank=True)
    tag = models.ManyToManyField(Tags, verbose_name='Ключевые слова к работе')

    def get_absolute_url(self):
        return reverse('about-work', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Работу'
        verbose_name_plural = 'Работы'
        ordering = ['-title']


class WorkScreenshots(models.Model):
    work = models.ForeignKey(Works, related_name='screenshots', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Скриншот работы', upload_to='image/works/screenshots/')

    class Meta:
        verbose_name = 'Скриншот работы'
        verbose_name_plural = 'Сриншот работы'