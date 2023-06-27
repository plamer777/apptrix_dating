"""There are a CBVs in the file to create, update, retrieve new raws in the
client table of the database"""
from rest_framework.generics import CreateAPIView
from participant.models import Client
from participant.serializers import ClientRegisterSerializer
# --------------------------------------------------------------------------


class CreateClientView(CreateAPIView):
    """This CBV serves to add new client to the database"""
    queryset = Client.objects.all()
    serializer_class = ClientRegisterSerializer
