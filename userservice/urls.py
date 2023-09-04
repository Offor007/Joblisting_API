from django.urls import path
from .views import UserListView, UserDetailView, SignUpView, LoginView, UserProfileView

urlpatterns = [
    path('users/', UserListView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/signup/', SignUpView.as_view(), name="user-signup"),
    path('users/login/', LoginView.as_view(), name="user-login"),
    path('users/profile/', UserProfileView.as_view(), name="user-profile"),
]
