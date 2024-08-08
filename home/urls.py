from django.urls import path
from home import views
from django.contrib import admin

# Admin Interface
admin.site.site_header = "ByteBandits"
admin.site.site_title = "Bandits Admin"
admin.site.index_title = "Cracking the Code of Excellence"


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('privacyPolicy', views.privacyPolicy, name='privacyPolicy'),
    path('Tos', views.Tos, name='Tos'),
]
