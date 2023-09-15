from . import views
from django.urls import path
app_name='animeapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('anime/<int:anime_id>/',views.detail,name='detail'),
    path('add/',views.add_anime,name='add_anime'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

    ]