from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('travels/', views.TravelListApiView.as_view(), name='travels'),
    path('travels/<int:pk>/', views.TravelDetailApiView.as_view(), name='travel'),
    path('categories/', views.TravelCategoryListApiView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.TravelCategoryDetailApiView.as_view(), name='category'),
    path('hotels/', views.HotelListApiView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', views.HotelDetailApiView.as_view(), name='hotel'),
]