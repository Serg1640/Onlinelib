from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('search-book/', views.search_book, name='search'),
    path('book_page/<str:pk>/', views.book_page, name='book'),
]
