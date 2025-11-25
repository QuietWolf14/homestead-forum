from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'forum'

urlpatterns = [
    path('', views.forum_home_view, name='home'),
    path('forum/<int:forum_id>/', views.forum_view, name='forum'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('post/new/', views.create_post, name='new_post'),
    path('post/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('comment/new/', views.create_comment, name='new_comment'),
    path('comment/<int:comment_id>/edit', views.edit_comment, name='edit_comment'),
    path('profile/<str:username>/', views.user_profile_view, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)