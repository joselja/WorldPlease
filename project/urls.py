"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ads.api import PostListAPI, PostDetailAPI, UserPostListAPI
from ads.views import CreatePostView, HomeView, PostDetailView, BlogDetailView
from blogs.views import BlogListView
from users.api import BlogsAPI, UsersAPI, UserDetailAPI
from users.views import LoginView, LogoutView, CreateUserView







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('blogs', BlogListView.as_view()),
    path('blogs/<str:username>', BlogDetailView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('new-post', CreatePostView.as_view(), name='new_post'),
    path('signup', CreateUserView.as_view(), name='new_user'),


    path('api/v1/users/', UsersAPI.as_view(), name='api-users'),
    path('api/v1/users/<int:pk>/', UserDetailAPI.as_view(), name='api-user-detail'),
    path('api/v1/posts/', PostListAPI.as_view(), name='api-posts'),
    path('api/v1/posts/<int:pk>/', PostDetailAPI.as_view(), name='api-post-detail'),
    path('api/v1/posts/mine/', UserPostListAPI.as_view(), name='api-user-mine'),
    path('api/v1/blogs/', BlogsAPI.as_view(), name='api-blogs'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
