from rest_framework import viewsets
from ..reviews import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

