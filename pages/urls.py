from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.BLogDetailView.as_view(), name='post_detail'),
]