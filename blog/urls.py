from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
   path('', views.IndexView.as_view(), name="index"),
   path('post/<int:post_id>', views.DetailsView.as_view(), name='details'),
   path('post/user_post', views.UserPostsView.as_view(), name='user-post'),
   path('post/new', views.PostCreateView.as_view(), name='new-post'),
   path('post/edit_post/<int:post_id>', views.PostUpdateView.as_view(), name='edit-post'),
   path('post/comment/<int:post_id>', views.CommentView.as_view(), name='add-comment'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

