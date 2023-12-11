"""projectII URL Configuration

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
from django.urls import path, include, re_path
from djangoPartII import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^help/', include('djangoPartII.urls')),
    # path('help', views.help, name = "help page"),
    path('admin/', admin.site.urls),
    path('research', views.research, name= 'research'),
    path('friends', views.friends, name='friends'),
    path('formpage', views.form_name_view, name='FormUsage'),
    path('insta/<str:username>/', views.instagram_posts_view, name='insta')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
