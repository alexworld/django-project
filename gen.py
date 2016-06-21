#!/usr/bin/env python

import django
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coolsite.settings")
django.setup()

from blog.models import Person, Tag, Post, Comment, PostPlus, CommentPlus
from django.db.utils import IntegrityError
from random import *

def random_str(maxlen=30):
    n = randint(1, maxlen)
    char_set = list(map(chr, list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1)) + [ord('_')]))
    return ''.join([choice(char_set) for i in range(n)])

def gen_person(num):
    Person.objects.bulk_create([Person(first_name=random_str(), last_name=random_str(), mode_restricted=randint(0, 1),
    password=random_str(), rating=randint(-100000, 100000), username=random_str()) for i in range(num)])

def gen_tag(num):
    Tag.objects.bulk_create([Tag(name=random_str()) for i in range(num)])

def gen_post(num):
    for x in range(num):
        now = Post.objects.create(name=random_str(), author=Person.objects.all()[randint(0, 100000)], restricted=randint(0, 1),
        rating=randint(-10000, 10000), text=random_str(1000))

        for i in range(randint(2, 10)):
            now.tag.add(Tag.objects.all()[randint(0, 1219)])

def gen_comment(num):
    i = 0
    Comment.objects.bulk_create([Comment(author=Person.objects.all()[randint(0, 100000)], post=Post.objects.all()[randint(0, 100000)], rating=randint(-1000, 1000),
    text=random_str(100)) for i in range(num)])

def gen_post_plus(num):
    i = 0
    PostPlus.objects.bulk_create([PostPlus(plus=randint(0, 1), author=Person.objects.all()[randint(0, 100000)], post=Post.objects.all()[randint(0, 100000)])
    for i in range(num)])

def gen_comment_plus(num):
    i = 0
    CommentPlus.objects.bulk_create([CommentPlus(plus=randint(0, 1), author=Person.objects.all()[randint(0, 100000)], comment=Comment.objects.all()[randint(0, 100000)])
    for i in range(num)])

def gen(num, func):
    i = 0

    while i < num:
        try:
            func(min(num - i, 100))
            i += min(num - i, 100)

            print(i)
        except IntegrityError:
            pass
    print 'Generated ' + func.__name__[func.__name__.find('_') + 1: ]

def clear():
    Person.objects.filter(is_superuser=False).delete()
    Tag.objects.all().delete()
    Post.objects.all().delete()
    Comment.objects.all().delete()
    PostPlus.objects.all().delete()
    CommentPlus.objects.all().delete()

def proc(Class, start):
    n = len(Class.objects.all())

    for i in range(start, n):
        pk = Class.objects.all()[i].pk
        Class.objects.all().filter(pk=pk).update(rating=Class.objects.all()[i].get_rating)

        if i % 100 == 0:
            print(Class.objects.all()[i].rating)
            print(Class.objects.all()[i].get_rating)
            print(i)

Person.objects.create(first_name='lol', last_name='lol', mode_restricted=1,
    password='lol', rating=179, username='lol')
