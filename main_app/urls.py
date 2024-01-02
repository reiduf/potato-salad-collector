from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('potatoes/', views.potatoes_index, name='index'),
  path('potatoes/<int:potato_id>/', views.potatoes_detail, name='detail'),
  path('potatoes/create/', views.PotatoCreate.as_view(), name='potatoes_create'),
  path('potatoes/<int:pk>/update', views.PotatoUpdate.as_view(), name='potatoes_update'),
  path('potatoes/<int:pk>/delete', views.PotatoDelete.as_view(), name='potatoes_delete'),
  path('potatoes/<int:potato_id>/add_comment/', views.add_comment, name='add_comment'),
]