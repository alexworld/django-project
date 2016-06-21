from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post, Person, Tag, Comment, PostPlus, CommentPlus
from django.http import Http404
from datetime import *
from .forms import UserForm, PostForm, CommentForm
from django.template import RequestContext
from django.template.loader import render_to_string

def getuser(request, strict=False):
    if request.user.is_authenticated():
        return request.user
    else:
        if strict:
            raise Http404("No such user")
        return None

def post_list(request, target = 0, page = 0):
    owner = getuser(request)
    page = int(page)
    pages = ['fresh', 'best', 'legend']
    target = int(target)

    if target < 0 or target > 2:
        raise Http404("No such page")

    if pages[target] == 'fresh':
        now = Post.objects.all().order_by('-release_date')[page * 20: page * 20 + 20]
    elif pages[target] == 'best':
        enddate = date.today()
        startdate = enddate - timedelta(days=1)
        now = Post.objects.all().filter(release_date__range=[startdate, enddate]).order_by('-rating')[page * 20: page * 20 + 20]
    else:
        now = Post.objects.all().order_by('-rating')[page * 20: page * 20 + 20]
    
    return render_to_response('blog/post_list.html', RequestContext(request, {'post_list': now, 'next_page': page + 1,
    'prev_page': max(page - 1, 0), 'target': target, 'owner': owner}))

def post_detail(request, pk):
    owner = getuser(request)
    post = get_object_or_404(Post, pk=pk)
    return render_to_response('blog/post_detail.html', RequestContext(request, {'post': post, 'owner': owner}))

def profile(request, pk):
    owner = getuser(request)
    person = get_object_or_404(Person, pk=pk)
    posts = Post.objects.all().filter(author=person)
    return render_to_response('blog/profile.html', RequestContext(request, {'person': person, 'posts': posts, 'owner': owner}))

def user_list(request):
    owner = getuser(request)
    return render_to_response('blog/user_list.html', RequestContext(request, {'user_list': Person.objects.all(), 'owner': owner}))

from django.contrib.auth import authenticate, login
from django import forms
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if not user_form.is_valid():
            html = render_to_string('blog/register.html', RequestContext(request, {'user_form': user_form}))
            return HttpResponse(html)

        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        Person.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        return redirect("/")
    else:
        user_form = UserForm()
        return render_to_response('blog/register.html', RequestContext(request, {'user_form': user_form}))
            
from django.contrib.auth.forms import AuthenticationForm
import django

def login(request):
    if request.method == 'POST':
        user_form = AuthenticationForm(data=request.POST)

        if not user_form.is_valid():
            html = render_to_string('blog/login.html', RequestContext(request, {'user_form': user_form}))
            return HttpResponse(html)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            django.contrib.auth.login(request, user)
        return redirect("/");
    else:
        user_form = AuthenticationForm()
        return render_to_response('blog/login.html', RequestContext(request, {'user_form': user_form}))


def logout(request):
    if request.method == 'POST':
        user = getuser(request)

        if user is not None:
            django.contrib.auth.logout(request)
            print('Loggouted ', user)
    return redirect("/")

def post_plus(request):
    if request.method == 'POST':
        owner = getuser(request, strict=True)
        post = request.POST.get('object')
        plus = request.POST.get('plus')
        print(post, plus)

        now = PostPlus.objects.filter(author=owner, post=post)

        if len(now) > 0 and now[0].plus == plus:
            raise Http404("Not allowed")

        if len(now) > 0 and now[0].plus != plus:
            now.delete()

        PostPlus.objects.create(author=owner, post=Post.objects.get(pk=int(post)), plus=int(plus))
        return redirect("/")

def comment_plus(request):
    if request.method == 'POST':
        owner = getuser(request, strict=True)
        comment = request.POST.get('object')
        plus = request.POST.get('plus')
        print(comment, plus)

        now = CommentPlus.objects.filter(author=owner, comment=comment)

        if len(now) > 0 and now[0].plus == plus:
            raise Http404("Not allowed")

        if len(now) > 0 and now[0].plus != plus:
            now.delete()

        CommentPlus.objects.create(author=owner, comment=Comment.objects.get(pk=int(comment)), plus=int(plus))
        return redirect("/")

def create_post(request):
    if request.method == 'POST':
#        post_form = PostForm(request.POST)

#        if not post_form.is_valid():
#            html = render_to_string('blog/create_post.html', RequestContext(request, {'post_form': post_form}))
#            return HttpResponse(html)

        owner = getuser(request, strict=True)
        name = request.POST.get('name')
        text = request.POST.get('text')

        Post.objects.create(author=owner, name=name, text=text)
        return redirect("/")
    else:
        post_form = PostForm()
        return render_to_response('blog/create_post.html', RequestContext(request, {'post_form': post_form}))

def edit_post(request, pk):
    if request.method == 'POST':
        owner = getuser(request, strict=True)
        name = request.POST.get('name')
        text = request.POST.get('text')
        
        if Post.objects.get(pk=pk).author == owner:
            Post.objects.filter(pk=pk).update(name=name)
            Post.objects.filter(pk=pk).update(text=text)
        return redirect("/")
    else:
        post_form = PostForm(instance=Post.objects.get(pk=pk))
        return render_to_response('blog/edit_post.html', RequestContext(request, {'post_form': post_form, 'post': pk}))

def create_comment(request, post):
    if request.method == 'POST':
        owner = getuser(request, strict=True)
        post = Post.objects.get(pk=int(post))
        text = request.POST.get('text')
        print(owner, post, text)

        Comment.objects.create(author=owner, post=post, text=text)
        return redirect("/")
    else:
        comment_form = CommentForm()
        return render_to_response('blog/create_comment.html', RequestContext(request, {'comment_form': comment_form, 'post': post}))

def edit_comment(request, post, pk):
    if request.method == 'POST':
        owner = getuser(request, strict=True)
        post = Post.objects.get(pk=int(post))
        text = request.POST.get('text')
        print(owner, post, text)

        if Comment.objects.get(pk=pk).author == owner:
            Comment.objects.filter(pk=pk).update(text=text)

        return redirect("/")
    else:
        comment_form = CommentForm(instance=Comment.objects.get(pk=pk))
        return render_to_response('blog/edit_comment.html', RequestContext(request, {'comment_form': comment_form, 'post': post, 'comment': pk}))
