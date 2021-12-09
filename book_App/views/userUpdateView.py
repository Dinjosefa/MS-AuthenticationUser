from django.conf import settings
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from book_App.serializers.userSerializers import UserSerializer
from django.forms.models import model_to_dict 
from book_App.models.user import User
from rest_framework.views import APIView
from django.http import JsonResponse

class UserUpdateView(generics.UpdateAPIView): 

   def put(self, request, *args, **kwargs): 
       pk = kwargs["pk"] 
       instance = User.objects.get(pk=pk) 
       request.data["username"] = instance.username
       request.data["password"] = instance.password
       request.data["is_superuser"] = instance.is_superuser
       serializer = UserSerializer(instance=instance, data=request.data) 
       serializer.is_valid(raise_exception=True) 
       serializer.update(instance, validated_data=request.data) 
       return Response(model_to_dict(instance), status=status.HTTP_201_CREATED)


        
        