
from django.urls import path

from apps.user.views import DeleteUserView, GoogleLoginView, UserAccountDeactivatePermissionView,  UserAccountListView, UserAccountReactivatePermissionView
urlpatterns = [
    path('google/logincreate/', GoogleLoginView.as_view(), name='login_google'),
    path('deleteall', DeleteUserView.as_view(), name='delete_user'),
    path('list-users', UserAccountListView.as_view(), name='list_users'),
    path('descativate_permission', UserAccountDeactivatePermissionView.as_view(),
         name='permision_deactivate_user'),
    path('ativate_permission', UserAccountReactivatePermissionView.as_view(),
         name='permision_activate_user'),
]
