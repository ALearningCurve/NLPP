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
    path("textExtractor/", views.file_upload, name="upload"),
    path("<int:pk>/delete/", views.DeletePost.as_view(), name="delete"),
    path("<int:pk>/update/", views.UpdatePost.as_view(), name="update"),

    path("<int:post_info_pk>/<int:method>", views.MemberInfoDetail, name="member_info"),

    path("<int:post_pk>/<int:post_member_pk>/<int:method>/graph/", views.graph, name="graph"),
    #path("<int:post_pk>/graph/", views.graph, name="graph"),

]
