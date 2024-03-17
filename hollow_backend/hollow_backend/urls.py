"""hollow_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from hollow_api.views import hello_world
from hollow_api.login import user_login
from hollow_api.creatAccount import create_account
from hollow_api.post import create_post
from hollow_api.get_post import get_posts
from hollow_api.get_user_info import get_user
from hollow_api.get_userPost import get_user_post
from hollow_api.follow import follow_user
from hollow_api.get_follow import get_follow
from hollow_api.unfollow import unfollow_user
from hollow_api.favorite import add_favorite
from hollow_api.get_postselectedCoursesString import get_selected_courses
from hollow_api.get_favorate import get_user_favorite_posts
from hollow_api.get_admin import get_admin
from hollow_api.delete_admin import admin_delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello-world/', hello_world, name='hello_world'),
    path('api/login/', user_login, name='login'),
    path('api/creatAccount/', create_account, name='create_account'),
    path('api/post/', create_post, name='post'),
    path('api/get_post/', get_posts, name='get_posts'),
    path('api/get_user/', get_user, name='get_user'),
    path('api/get_userPost/', get_user_post, name='get_userPost'),
    path('api/follow/', follow_user, name='follow_user'),
    path('api/get_follow/', get_follow, name='get_follow'),
    path('api/unfollow/', unfollow_user, name='unfollow_user'),
    path('api/add_favorite/', add_favorite, name='add_favorite'),
    path('api/get_postselectedCoursesString/', get_selected_courses, name='get_selected_courses'),
    path('api/get_user_favorite_posts/', get_user_favorite_posts, name='get_user_favorite_posts'),
    path('api/get_admin/', get_admin, name='get_admin'),
    path('api/admin_delete/', admin_delete_post, name='admin_delete_post'),
]
