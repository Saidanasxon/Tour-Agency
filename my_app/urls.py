from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('travels/', views.TravelAPIView.as_view(), name='travels'),
    path('travels/<int:pk>/', views.TravelAPIView.as_view(), name='travel'),
    path('categories/', views.TravelCategoryAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.TravelCategoryAPIView.as_view(), name='category'),
    path('hotels/', views.HotelAPIView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', views.HotelAPIView.as_view(), name='hotel'),
    
]