from django.contrib.auth.models import User
from rest_framework import viewsets
from membersapp.serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """ Endpoint for users """

    queryset = User.objects.all().order_by()
    serializer_class = UserSerializer
