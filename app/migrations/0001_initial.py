# Generated by Django 3.1.8 on 2021-05-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('add_time', models.CharField(max_length=32, verbose_name='添加时间')),
                ('editor', models.CharField(max_length=32, verbose_name='编辑')),
            ],
            options={
                'verbose_name': '爬虫数据表',
                'verbose_name_plural': '爬虫数据表',
            },
        ),
    ]