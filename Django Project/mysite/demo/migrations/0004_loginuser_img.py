# Generated by Django 2.1.3 on 2018-11-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_loginuser_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='img',
            field=models.ImageField(default='1', upload_to='img'),
            preserve_default=False,
        ),
    ]