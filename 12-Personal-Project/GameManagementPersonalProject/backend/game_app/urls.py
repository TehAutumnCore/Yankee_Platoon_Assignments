from django.urls import path
from .views import GameViewAll, GameViewDetail, GameViewUpdate, GameViewDelete

urlpatterns = [
    path('', GameViewAll.as_view(), name='game-list'),
    path('<int:id>/',GameViewDetail.as_view(), name='game-detail' ),
    path('<int:id>/update/',GameViewUpdate.as_view(), name='game-update' ),
    path('<int:id>/delete/',GameViewDelete.as_view(), name='game-delete' )
]