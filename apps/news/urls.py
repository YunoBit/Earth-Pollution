from django.urls import path 

from apps.news import views


urlpatterns = [
    path('',views.NewsListView.as_view(),name='index'),
    path('create/',views.NewsCreateView.as_view(),name='create'),
    path('detail/<int:pk>/',views.NewsDetailView.as_view(),name='detail'),
    path('update/<int:pk>/', views.NewsUpdateView.as_view(),name='update'),
    path('detele/<int:pk>/',views.NewsDeleteView.as_view(),name='delete'),
]
