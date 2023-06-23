from django.urls import path
from .views import *

urlpatterns = [
    #path('', index, name='index'),
    #path('category/<int:pk>/', category_list, name='category_list'),
    #path('post/<int:pk>/', post_detail, name='post_detail'),
    #path('add_article/', add_post, name='add'),
    path('', Index.as_view(), name='index'),
    path('category/<int:pk>/', ArticleByCategory.as_view(), name='category_list'),
    path('post/<int:pk>/', ArticleDetail.as_view(), name='post_detail'),
    path('add_article/', NewArticle.as_view(), name='add'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('post/<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('search/', SearchResults.as_view(), name='search_results'),
    path('add_comment/<int:article_id>/', add_comment, name='add_comment')

]