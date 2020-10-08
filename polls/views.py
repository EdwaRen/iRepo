# from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import ImageViewForm
from .models import ImageView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from polls.serializers import UserSerializer, GroupSerializer, ImageViewSerializer


class HomePageView(ListView):
    model = ImageView
    template_name = 'home.html'

class CreateImageViewView(CreateView):
    model = ImageView
    form_class = ImageViewForm
    template_name = "post.html"
    success_url = reverse_lazy('home')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ImageView.objects.all()
    serializer_class = ImageViewSerializer
    permission_classes = [permissions.IsAuthenticated]