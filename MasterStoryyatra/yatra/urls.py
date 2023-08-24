from django.urls import path
from yatra import views

urlpatterns = [
     path('', views.index, name='index'),
     path('about/', views.about, name='about'),
     path('detailed_blog/<int:id>/', views.detailed_blog_view, name='detailed_blog'),
     path('like-post/<int:post_id>/', views.likecount, name='likecount'),
     path('create_post/', views.create_post, name='create_post'),
     path('search_results/', views.search, name='search'),
     # path('post_comment/<int:post_id>/', views.post_comment, name='post_comment'),
     path('reply_comment/<int:comment_id>/', views.reply_comment, name='reply_comment'),

     path('navbar/', views.navbar_data, name='navbar_data'),
     path('nation-detail/<str:cname>/', views.NationDetails, name='NationDetails'),
     path('get-state-blog/', views.get_state_blog, name='get_state_blog'),

]

