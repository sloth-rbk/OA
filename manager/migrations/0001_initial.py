# Generated by Django 2.2.9 on 2020-02-24 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manageradmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Xmsqd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xqid', models.CharField(max_length=20, verbose_name='需求编号')),
                ('xmname', models.CharField(max_length=20, verbose_name='项目名称')),
                ('xmdiqu', models.CharField(max_length=10, verbose_name='需求地区')),
                ('xqry', models.CharField(max_length=10, verbose_name='所需人数')),
                ('ryjn', models.CharField(max_length=50, verbose_name='人员技能')),
                ('bzxx', models.CharField(max_length=100, verbose_name='备注信息')),
                ('kstime', models.DateField(blank=True, default=None, verbose_name='开始时间')),
                ('jstime', models.DateField(blank=True, default=None, verbose_name='结束时间')),
                ('cjtime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('xqcltime', models.DateField(blank=True, default=None, null=True, verbose_name='需求处理时间')),
                ('zhuangtai',
                 models.IntegerField(choices=[(0, '待审核'), (1, '受理'), (2, '驳回'), (3, '待评价'), (4, '完成')], default=0,
                                     verbose_name='状态')),
                ('clbz', models.CharField(max_length=100, verbose_name='处理备注')),
                ('access', models.TextField(verbose_name='人员评价')),
                ('fpry', models.ManyToManyField(to='manageradmin.Tjd_staff')),
                ('xmjl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
