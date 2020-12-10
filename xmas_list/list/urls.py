from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('edit_list', views.edit_list, name='edit_list'),
    path('delete_gift/<int:gift_id>', views.delete_gift, name='delete_gift'),
    path('claim_gift/<int:gift_id>', views.claim_gift, name='claim_gift'),
    path('unclaim_gift/<int:gift_id>', views.unclaim_gift, name='unclaim_gift'),
    path('account', views.account, name='account'),
    path('change_password', views.change_password, name='change_password'),
    path('update_account_info', views.update_account_info, name='update_account_info'),
    path('login/', views.login_request, name='login_request'),
    path('logout/', views.logout_request, name='logout_request'),
    # path('change-password', auth_views.PasswordChangeView.as_view(success_url="/"), name='change-password'),
    path('robots.txt', views.robots, name='robots'),
]
