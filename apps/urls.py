from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import (
    BookListAPIView, AuthorListAPIView, ProductListAPIView
)

urlpatterns = [
    path('auth/refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('books', BookListAPIView.as_view()),
    path('authors', AuthorListAPIView.as_view()),
    path('products', ProductListAPIView.as_view())

]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
