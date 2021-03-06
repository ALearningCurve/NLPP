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
    path("<int:pk>/delete/", views.DeletePost.as_view(), name="delete"),
    path("<int:pk>/update/", views.UpdatePost.as_view(), name="update"),

    path("<int:post_info_pk>/<int:method>", views.member_info_detail, name="member_info"),
    path("<int:pk>/member_info/<int:method>", views.collective_member_info_detail, name="collective_member_info"),

    path("textExtractor/", views.file_upload, name="upload"),
    # Uncomment this to see the test page or the graph page
    # Graph page is not yet fully functional
    #path("<int:post_pk>/<int:post_member_pk>/<int:method>/graph/", views.graph, name="graph"),
    #path("test/", views.test, name = "test")
]
