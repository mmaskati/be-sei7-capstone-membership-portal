from django.urls import path,include
from . import views
from .views import ManageLogin


app_name="bussines_portal_app"
urlpatterns = [
    path('',views.home, name='home'),
    path('organization/',views.OrganizationList.as_view(),name='organization_index'),
    path('organization/create/',views.OrganizationCreate.as_view(),name='organization_create'),
    path('organization/<int:pk>/update/',views.OrganizationUpdate.as_view(),name='organization_update'),
    path('organization/<int:pk>/delete/',views.OrganizationDelete.as_view(),name='organization_delete'),
    path('organization/<int:pk>/',views.OrganizationDetail,name='organization_detail'),
    
    path('profile/<int:pk>/update',views.ProfileUpdate.as_view(),name='profile_update'),
    path('profile/',views.ProfileList.as_view(),name='profile_index'),
    path('organization/<int:user_id>/remove/<int:organization_id>',views.remove_member,name='remove_member'),

    path('login/', ManageLogin.as_view(), name='login'),

 # yousif added the planFeature
    # path('plan/feature/',views.PlanList.as_view(),name='plan_feature_index'),
    # path('plan/feature/<int:pk>/update/',views.PlanUpdate.as_view(),name='plan_feature_update'),
    # path('plan/feature/<int:pk>/delete/',views.PlanDelete.as_view(),name='plan_feature_delete'),
    # yousif added the plan
    path('plan/',views.PlanList.as_view(),name='plan_index'),
    path('plan/create/',views.PlanCreate.as_view(),name='plan_create'),
    path('plan/<int:pk>/update/',views.PlanUpdate.as_view(),name='plan_update'),
    path('plan/<int:pk>/delete/',views.PlanDelete.as_view(),name='plan_delete'),
    

    path('events/',views.EventList.as_view(),name='events_index'),
    path('events/create/',views.EventCreate.as_view(),name='events_create'),
    path('events/<int:pk>/update/',views.EventUpdate.as_view(),name='events_update'),
    path('events/<int:pk>/delete/',views.EventDelete.as_view(),name='events_delete'),
    path('events/<int:pk>/',views.EventDetail.as_view(),name='events_detail'),


]
