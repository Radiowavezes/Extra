from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/create_data/', views.create_data, name='create_data'),
    path('update/<int:id_num>', views.update, name='update'),
    path('update/update_data/<int:id_num>', views.update_data, name='update_data'),
    path('delete/<int:id_num>', views.delete, name='delete'),
    ]