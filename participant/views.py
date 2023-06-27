"""There are a CBVs in the file to create, update, retrieve new raws in the
client table of the database"""
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from participant.models import Client
from participant.serializers import (
    ClientRegisterSerializer, ClientUpdateSerializer)
from utils import send_message
# --------------------------------------------------------------------------


class CreateClientView(CreateAPIView):
    """This CBV serves to add new client to the database"""
    queryset = Client.objects.all()
    serializer_class = ClientRegisterSerializer


class UpdateClientView(UpdateAPIView):
    """This CBV serves to add new client to the database"""
    serializer_class = ClientUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Client.objects.filter(email=self.request.user.email)
        return queryset

    def get_object(self):
        return Client.objects.get(email=self.request.user.email)

    def partial_update(self, request, *args, **kwargs):
        current_client = Client.objects.get(email=self.request.user.email)
        favorite = Client.objects.filter(pk=self.kwargs.get(
            'favorite_id')).first()
        if not favorite:
            raise ValidationError(
                {'message': 'The client with the given pk is not found'})
        elif favorite.pk == current_client.pk:
            raise ValidationError(
                {'message': 'You cannot add yourself as a favorite'})

        current_client.favorites.add(favorite)
        super().partial_update(request, *args, **kwargs)

        if favorite.favorites.filter(pk=current_client.pk).exists():
            send_message(current_client, favorite)
            send_message(favorite, current_client)
            return JsonResponse({'favorite_email': favorite.email})

        return JsonResponse({'message': 'Favorite added successfully'})
