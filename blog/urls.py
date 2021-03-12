from django.urls import path, include

from . import views

urlpatterns = [
   path('', views.IndexView.as_view(), name="index"),
   path('post/<int:post_id>', views.DetailsView.as_view(), name='details'),
]