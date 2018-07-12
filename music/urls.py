from django.urls import path
app_name = 'music'

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:album_id>/', views.detail, name = 'detail'),

    # /music/album_id/favourite/
    path('<int:album_id>/favourite/',views.favourite, name = 'favourite'),
]
