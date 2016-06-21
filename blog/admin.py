from django.contrib import admin
from .models import Person, Tag, Post, Comment, PostPlus, CommentPlus
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostPlus)
admin.site.register(CommentPlus)
