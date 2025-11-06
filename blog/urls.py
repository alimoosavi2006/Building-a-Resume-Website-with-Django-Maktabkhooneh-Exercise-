from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("blogs-page.html", home_view_blog, name="home_blog_page"),
    path("single/",single_blog,name="single_blog"),
]