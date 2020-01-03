from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('all/', views.ListGroups.as_view(), name="all"),
    path('find/', views.group_find, name="find"),
    path("new/", views.CreateGroup.as_view(), name="create"),
    path("<slug>/delete/", views.DeleteGroup.as_view(), name="delete"),
    path("singular/<slug>/",views.SingleGroup.as_view(),name="single"),
    path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
    path("singular/<slug>/kick/<pk>/",views.KickUserGroup.as_view(),name="kick"),
    # path("update/<slug>",views.UpdateGroup.as_view(),name="update"),
]
