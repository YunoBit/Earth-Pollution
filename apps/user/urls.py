from django.urls import path

from apps.user import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('login/',views.LoginView.as_view(), name='login')
]
