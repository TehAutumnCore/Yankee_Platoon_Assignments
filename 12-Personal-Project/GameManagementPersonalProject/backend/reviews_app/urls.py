from django.urls import path
from .views import ReviewViewAll, ReviewViewUpdate, ReviewViewDelete

urlpatterns = [
    path('', ReviewViewAll.as_view(), name='review-list'),
    path('<int:id>/update/', ReviewViewUpdate.as_view(), name='review-update'),
    path('<int:id>/delete/', ReviewViewDelete.as_view(), name='review-delete'),
]