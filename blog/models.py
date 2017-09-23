# coding=utf-8
from collections import defaultdict

from django.db import models


class ArticleManager(models.Manager):

    def archive(self):
        data_list = Article.objects.datetimes('created_time', 'month', order='DESC')
        data_dict = defaultdict(list)
        for d in data_list:
            data_dict[d.year].append(d.month)

        return sorted(data_dict.items(), reverse=True)


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    objects = ArticleManager()
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=254, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前254个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类', 
                                 null=True, 
                                 on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']

    def save(self, *args, **kwargs):
        if not self.abstract:
            self.abstract = self.body[:254]
        super(Article, self).save()


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name



