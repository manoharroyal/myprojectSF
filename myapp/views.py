from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from utils import login
from serializers import ContactSerializer
from models import Contact
from rest_framework.response import Response
# Create your views here.


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def contact(self, request):
        sf = login()

        if request.method == 'POST':
            data = request.data.copy()
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                return_dict = serializer.validated_data
                query = sf.Contact.create(return_dict)
                return Response(query)
            else:
                return Response(serializer.errors)
        else:
            data = sf.query("Select Id,Name from Contact")
            result = ContactSerializer(data['records'][0])
            return Response(result.data)
