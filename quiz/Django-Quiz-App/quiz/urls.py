"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.RegisterUser, name="register"),
    path('addquestion', views.add_question, name="addquestion"),
    path('randompage', views.randompage, name="randompage"),
    path('python', views.python, name="python"),
    path('dbms', views.dbms, name="dbms"),
    path('basic', views.basic, name="basic"),
    path('intermediate', views.intermediate, name="intermediate"),
    path('expert', views.expert, name="expert"),
    path('results', views.results, name="results"),
    path('profile', views.profile, name="profile"),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Quizzies Admin"
admin.site.site_title = "Quizzies Admin Portal"
admin.site.index_title = "Welcome to Quizzies Researcher Portal"