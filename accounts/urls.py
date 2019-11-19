from django.urls import path, include
from . import views
from rest_framework import routers

# router =  routers.DefaultRouter()
# router.register('books', views.BookView)
# router.register('authors', views.AuthorView)
# router.register('publications', views.PublicationView)
# router.register('languages', views.LanguageView)

urlpatterns = [
    path('register/', views.create_user, name='user-register'),
    path('logout/', views.logout, name='user-logout'),
]
