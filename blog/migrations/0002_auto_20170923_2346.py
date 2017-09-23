# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(help_text=b'\xe5\x8f\xaf\xe9\x80\x89\xef\xbc\x8c\xe5\xa6\x82\xe8\x8b\xa5\xe4\xb8\xba\xe7\xa9\xba\xe5\xb0\x86\xe6\x91\x98\xe5\x8f\x96\xe6\xad\xa3\xe6\x96\x87\xe7\x9a\x84\xe5\x89\x8d254\xe4\xb8\xaa\xe5\xad\x97\xe7\xac\xa6', max_length=254, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe9\x9b\x86\xe5\x90\x88', blank=True),
        ),
    ]
