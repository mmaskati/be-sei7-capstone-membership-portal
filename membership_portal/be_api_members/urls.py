from django.urls import path
from . import views

urlpatterns = [
    path('user/list', views.user_list, name = 'user_list'),
    path('benefit/list', views.benefit_list, name = 'benefit_list'),
    path('benefit/adduser', views.benefit_add_user, name = 'benefit_add_user'),
    path('benefit/detail/', views.benefit_detail, name = 'benefit_detail'),
    path('benefit/qrcode', views.benefit_qrcode, name = 'benefit_qrcode'),
    path('benefit/delete', views.benefit_delete, name = 'benefit_delete'),
    path('benefit/create', views.benefit_create, name = 'benefit_create'),
    path('benefit/update', views.benefit_update, name = 'benefit_update'),  
    path('login/',views.LoginAPIView.as_view(),name='login')  
    # Test model
    # path('test/create', views.test_create, name = 'test_create'),
]