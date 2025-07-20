from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu/', views.MenuItemList.as_view(),name='menuItem-list'),
    path('menu/<int:pk>/', views.MenuItemDetail.as_view(), name ='menuItem-detail'),
    path('orders/', views.OrderListcreate.as_view(), name= 'orderlist'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name= 'order-details'),
    path('Register/', views.RegisterUser.as_view, name= 'register'),
    path('api/token/', obtain_auth_token, name = 'obtain')

]