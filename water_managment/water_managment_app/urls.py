
from django.contrib import admin
from django.urls import path

from water_managment_app.views import  *

urlpatterns = [
    # ////////////////////////////////// ADMIN ///////////////////////////////////
    path('',Login_page.as_view(),name='login'),
    path('admin_home',AdminHome.as_view(),name='admin_home'),
    path('complaint',ComplaintPage.as_view(),name='complaint'),
    path('manage_sub_admin',ManageSubAdminPage.as_view(),name='manage_sub_admin'),
    path('add_subadmin',Addsubadmin.as_view(),name='add_subadmin'),
    path('DelSubAdmin/<int:id>/',DelSubAdmin.as_view(),name='DelSubAdmin'),
    path('Addarea',Addarea.as_view(),name='Addarea'),
    path('EditSubAdmin/<int:id>/',EditSubAdmin.as_view(),name='EditSubAdmin'),
    path('NotificationListView', NotificationListView.as_view(), name='notification_list'),
    path('create/', NotificationCreateView.as_view(), name='notification_create'),
    path('update/<int:pk>/', NotificationUpdateView.as_view(), name='notification_update'),
    path('delete/<int:pk>/', NotificationDeleteView.as_view(), name='notification_delete'),

    # ////////////////////////////// SUBADMIN ///////////////////////////////////

    path('connection',ConnectionPage.as_view(),name='connection'),
    path('SubAdminHome',SubAdminHome.as_view(),name="SubAdminHome"),
    path('Subadminprofile',Subadminprofile.as_view(),name="Subadminprofile"),
    path('meter_reader',Addmeterreader.as_view(),name="meter_reader"),
    path('approve_connection/<int:id>/',ApproveConnection.as_view(),name='approve_connection'),
    path('reject_connection/<int:id>/',RejectConnection.as_view(),name='reject_connection'),
    path('meter_reader/<int:id>/',Addmeterreader.as_view(),name='meter_reader'),
    path('ViewArea',ViewArea.as_view(),name='ViewArea'),
    path('EditArea/<int:id>/',EditArea.as_view(),name='EditArea'),
    path('DelArea/<int:id>/',DelArea.as_view(),name='DelArea'),
   
    path('change_password/<int:id>/',Changepassword.as_view(),name='change_password'),
    # ////////////////////////////// METERREADER ///////////////////////////////////
    path('view_payment/',ViewPayment.as_view(),name='view_payment'),
    path('view_profile/<int:id>/',ViewProfile.as_view(),name='view_profile'),
    path('connectionmeterreader',ConnectionPagemeterreader.as_view(),name='connectionmeterreader'),

]
