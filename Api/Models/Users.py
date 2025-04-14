from rest_framework import serializers,viewsets
from django.contrib.auth.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_login', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply filters based on query parameters
        username = self.request.query_params.get('username')
        email = self.request.query_params.get('email')
        if username:
            queryset = queryset.filter(username=username)
        elif email:
            queryset = queryset.filter(email=email)
        return queryset