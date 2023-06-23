from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Category, Post, Comment
from .forms import PostForm, LoginForm, RegistrationForm, CommentForm, UserProfileForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.db.models import Q


class Index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'web_site/index.html'
    extra_context = {
        'title': 'Home page'
    }


class ArticleByCategory(Index):
    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


class ArticleDetail(DetailView):
    model = Post
    template_name = 'web_site/article_detail.html'

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Post.objects.get(pk=self.kwargs['pk'])
        article.watched += 1
        article.save()
        context['title'] = f'Recipe: {article.title}'
        context['comments'] = Comment.objects.filter(post=article)
        posts = Post.objects.all()
        posts = posts.order_by('-watched')[:4]

        context['posts'] = posts

        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()

        return context


class NewArticle(CreateView):
    form_class = PostForm
    template_name = 'web_site/article_form.html'
    extra_context = {
        'title': 'Add recipe'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'web_site/article_form.html'


class ArticleDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = 'post'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You\'ve successfully logged in')
            return redirect('index')

    else:
        form = LoginForm()

    context = {
        'title': 'User authentication',
        'form': form
    }
    return render(request, 'web_site/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            # login(request, user)
            return redirect('login')

    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()
    context = {
        'title': 'User registration',
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'web_site/register.html', context)


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    articles = Post.objects.filter(author=user)
    context = {
        'title': f'{user.first_name} {user.last_name}',
        'user': user,
        'articles': articles
    }
    return render(request, 'web_site/profile.html', context)


class SearchResults(Index):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Post.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word)
        )
        return articles


def add_comment(request, article_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        post = Post.objects.get(pk=article_id)
        comment.post = post
        comment.save()
        messages.success(request, 'Your comment has been added successfully')
    else:
        pass
    return redirect('post_detail', article_id)
