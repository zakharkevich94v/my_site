from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_workscreenshots_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='screen_work',
        ),
    ]
