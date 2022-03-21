from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=35, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=45, null=True, verbose_name='Фамилия')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Аватарка')),
                ('email_addres', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email адрес')),
                ('link_github', models.URLField(blank=True, null=True, verbose_name='Ссылка на Гитхаб')),
                ('link_linkedin', models.URLField(blank=True, null=True, verbose_name='Ссылка на Linkedin')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автор',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Название тега')),
                ('slug', models.SlugField(max_length=35, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название проекта')),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='URL')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('work_preview', models.ImageField(blank=True, null=True, upload_to='image/works/', verbose_name='Превью работы')),
                ('screen_work', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Скриншот работы')),
                ('description', models.TextField(blank=True, verbose_name='Описание проекта')),
                ('link_source_code', models.URLField(blank=True, verbose_name='Ссылка на исходный код проекта')),
                ('link_webpage', models.URLField(blank=True, verbose_name='Ссылка на страницу проекта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='works', to='blog.category')),
                ('tag', models.ManyToManyField(to='blog.Tags', verbose_name='Ключевые слова к работе')),
            ],
            options={
                'verbose_name': 'Работу',
                'verbose_name_plural': 'Работы',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='WorkScreenshots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/works/screenshots/', verbose_name='Скриншот работы')),
                ('work', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.works')),
            ],
            options={
                'verbose_name': 'Скриншот работы',
                'verbose_name_plural': 'Сриншот работы',
            },
        ),
    ]
