import markdown
import logging

from django.conf import settings
from django.views.generic import DetailView
from django.views.generic.list import ListView
from blog.models import Article, Category, Tag


class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"
    paginate_by = settings.PAGE_NUM

    def get_queryset(self, *args, **kwargs):
        article_list = Article.objects.filter(status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['color_list'] = ['default', 'info', 'primary', 'warning', 'danger']
        return super(IndexView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = "blog/category.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['color_list'] = ['default', 'info', 'primary', 'warning', 'danger']
        return super(CategoryView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"
    pk_url_kwarg = "article_id"

    def get_object(self, *args, **kwargs):
        obj = super(ArticleDetailView, self).get_object()
        extension_list = ['markdown.extensions.extra',
                          'markdown.extensions.codehilite',
                          'markdown.extensions.toc',
                          'markdown.extensions.wikilinks']
        obj.body = markdown.markdown(obj.body, extensions=extension_list)
        return obj

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['color_list'] = ['default', 'info', 'primary', 'warning', 'danger']
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class TagView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['color_list'] = ['default', 'info', 'primary', 'warning', 'danger']
        return super(TagView, self).get_context_data(**kwargs)


class ArchiveView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['color_list'] = ['default', 'info', 'primary', 'warning', 'danger']
        return super(ArchiveView, self).get_context_data(**kwargs)