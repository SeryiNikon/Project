
"""homework_07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog import views
from blog.views import PostCommentView, PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView, \
    CategoryList, CategoryDetail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comment', PostCommentView.as_view(), name='post-comment'),
    path('create', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('home/', views.home, name="home"),
    path('home/signup/', views.SignUp.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    # path('/login', LoginView.as_view(), name='login'),
]
