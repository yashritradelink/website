from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('sendmail', views.sendmail, name='sendmail'),
    path('index', views.index, name='index'),
    #path('about',include('webapp-about.urls')),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    #path('blog', views.blog, name='blog'),
    path('service', views.service, name='service'),
    path('projectn', views.projectn, name='projectn'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    #path('blog', views.blog, name='blog'),
    #path('detail', views.detail, name='detail'),
    path('pp', views.pp, name='pp'),
    path('pe', views.pe, name='pe'),
    path('pet', views.pet, name='pet'),
    path('ps', views.ps, name='ps'),
    path('masterbatch', views.masterbatch, name='masterbatch'),
    path('recycled', views.recycled, name='recycled'),
]