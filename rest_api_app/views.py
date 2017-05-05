from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_api_app.serializers import UserSerializer, GroupSerializer, ProfileSerializer
from rest_api_app.models import Profile
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import throttle_classes, authentication_classes, permission_classes


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
   
   
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'
    # def retrieve(request, username):
    #     user = User.objects.get(username = username)
    #     print "asasdddddddddddddddddddsd"
    #     profile = Profile.objects.get(user = user)
    #     serializer = ProfileSerializers(profile , context={'request': request})
    #     return Response(serializer.data)
        
