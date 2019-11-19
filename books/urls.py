from django.urls import path, include
from . import views
from rest_framework import routers

# router =  routers.DefaultRouter()
# router.register('books', views.BookView)
# router.register('authors', views.AuthorView)
# router.register('publications', views.PublicationView)
# router.register('languages', views.LanguageView)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('books/', views.book_list, name='list-create-books'),
    path('books/update/<int:id>/', views.api_update_book_view, name='update-book'),
    path('book/<int:id>', views.api_view_delete_book, name='delete-bookss')
    # path('books/create/', views.api_create_book_view, name='create-book'),
]
