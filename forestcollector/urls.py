from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forest_collector, name='forrestcollector'),
    path('liste/', views.home, name='home'),
    path('video/', views.showvideo, name='showvideo'),
    path('register/', views.register, name='register'),
    path('<int:chapter>/<int:section>/', views.printSection, name='chapterContent'),
    path('accounts/', include('django.contrib.auth.urls')),
]
