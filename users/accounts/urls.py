from django.urls import path
from .views import UserDeatilAPIView


urlpatterns = [
    path('<username>/', UserDeatilAPIView.as_view(), name='user-detail'),
]
