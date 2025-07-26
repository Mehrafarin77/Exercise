from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.BLogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.BlogDeleteView.as_view(), name='post_delete'),
]