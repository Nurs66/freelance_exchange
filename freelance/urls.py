from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    OrderViewList,
    OrderCreateAPIView,
    OrderViewDetail,
    OrderViewDelete,
    OrderViewUpdate,
)

# API endpoints
urlpatterns = format_suffix_patterns([
    path('task/', TaskListView.as_view(), name='task'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:id>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:id>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:id>/', TaskDetailView.as_view(), name='task_details'),

    path('order/', OrderViewList.as_view(), name='order'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('order/<int:id>/', OrderViewDetail.as_view(), name='order_details'),
    path('order/<int:id>/delete/', OrderViewDelete.as_view(), name='order_delete'),
    path('order/<int:id>/update/', OrderViewUpdate.as_view(), name='order_update'),
])
