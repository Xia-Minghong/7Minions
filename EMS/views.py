from .serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework import permissions, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer