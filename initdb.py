#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
author:seck
time: 2018/01/26
"""
import random
from blog_week_5.wsgi import *
from Model_study.models import Author, Article, Tag

author_name_list = ['xjnu', 'seck', 'sfdx', 'test', 'xjseck']
article_title_list = ['Django 笔记', 'Python 学习', 'HTML 学习']


def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # 随机生成9位数的QQ，
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % (random.randrange(1, 3))
        author.email = '%s@seck.com' % (author.addr)
        author.save()


def create_articles_and_tags():
    # 随机生成文章
    for article_title in article_title_list:
        # 从文章标题中得到 tag
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)

        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '%s_%s' % (article_title, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,  # 随机分配作者
                    'content': '%s 正文' % title,
                    'score': random.randrange(70, 101),  # 随机给文章一个打分
                }
            )
            article.tags.add(tag)


def main():
    create_authors()
    create_articles_and_tags()


if __name__ == '__main__':
    main()
    print("Done!")