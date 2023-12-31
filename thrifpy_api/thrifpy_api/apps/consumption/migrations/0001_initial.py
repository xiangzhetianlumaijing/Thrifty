# Generated by Django 4.2.1 on 2023-08-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='描述信息')),
                ('consumption_time', models.DateTimeField(verbose_name='消费日期')),
                ('category', models.CharField(blank=True, max_length=10, null=True, verbose_name='消费类别')),
                ('consumption_way', models.CharField(max_length=20, verbose_name='交易方式')),
                ('is_necessary', models.BooleanField(default=True, verbose_name='是否必需')),
                ('amount', models.FloatField(verbose_name='消费金额')),
            ],
            options={
                'verbose_name': '消费信息',
                'verbose_name_plural': '消费信息',
                'db_table': 'consumption',
            },
        ),
    ]
