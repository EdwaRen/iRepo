from django.urls import path

from .views import HomePageView, CreateImageViewView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post_create/', CreateImageViewView.as_view(), name='add_post')  # new

]