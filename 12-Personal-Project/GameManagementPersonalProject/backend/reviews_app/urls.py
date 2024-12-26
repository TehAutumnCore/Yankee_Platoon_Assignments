from django.urls import path
from .views import ReviewViewAll, ReviewViewDetail

urlpatterns = [
    path('game/<int:game_id>/', ReviewViewAll.as_view(), name='review-list'),
    path('<int:id>/', ReviewViewDetail.as_view(), name='review-detail'),
]