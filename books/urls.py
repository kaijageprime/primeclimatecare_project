import uuid
from django.urls import path

from .views import BookListView, BookDetailView, SearchReasultsListView


urlpatterns = [

    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchReasultsListView.as_view(), name='search_results'),
    
    
]