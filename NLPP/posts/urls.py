from django.urls import path
from . import views

app_name = "posts"

'''
    path('<slug>/', views.PostList.as_view(), name="all"),


    # Decide paths for these
    path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
'''

urlpatterns = [
    path("new/", views.CreatePost.as_view(), name="create"),
    path("<int:pk>/",views.PostDetail.as_view(),name="single"),
]
