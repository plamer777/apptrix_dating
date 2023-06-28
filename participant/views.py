"""There are a CBVs in the file to create, update, retrieve new raws in the
client table of the database"""
from django.db.models import QuerySet
from django.http import JsonResponse
from haversine import haversine
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from participant.filters import ClientListFilter
from participant.models import Client
from participant.serializers import (
    ClientRegisterSerializer, ClientUpdateSerializer, ClientListSerializer)
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

    def get_queryset(self) -> QuerySet[Client]:
        """This method was rewritten to return a queryset only for current
        client
        :return: a QuerySet object
        """
        queryset = Client.objects.filter(email=self.request.user.email)
        return queryset

    def get_object(self) -> Client:
        """This method returns the client object for the current user
        :return: a Client object
        """
        return Client.objects.get(email=self.request.user.email)

    def update(self, request, *args, **kwargs) -> JsonResponse:
        """This method adds a new client to the favorites of the current client
        and sends emails if the clients have mutual sympathy
        :return: a JsonResponse object with the message containing the result
        of the operation or favorite email if sympathy was mutual
        """
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
        super().update(request, *args, **kwargs)

        if favorite.favorites.filter(pk=current_client.pk).exists():
            send_message(current_client, favorite)
            send_message(favorite, current_client)
            serializer = self.get_serializer_class()
            return JsonResponse(serializer(favorite).data)

        return JsonResponse({'message': 'Favorite added successfully'})


class ClientListView(ListAPIView):
    """This CBV serves to display a list of clients"""
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientListFilter

    def get_object(self) -> Client:
        """This method returns the client object for the current user
        :return: a Client object
        """
        return Client.objects.get(user=self.request.user)

    def get_queryset(self) -> QuerySet[Client]:
        """This method was rewritten to calculate a distance between current
        client and a list of all clients
        :return: a QuerySet of all clients
        """
        current_client = self.get_object()
        queryset = Client.objects.all()

        for client in queryset:
            try:
                client.distance = haversine(
                    (client.lat, client.lon),
                    (current_client.lat, current_client.lon))
            except Exception:
                client.distance = None

            client.save()

        return queryset
