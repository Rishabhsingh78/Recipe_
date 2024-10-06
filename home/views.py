from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingredients,Receipe
from .serializers import ReceipeSerializer

class ReceipeApi(APIView):
    def get(self,request):
        quertset = Receipe.objects.all()
        serializer = ReceipeSerializer(quertset,many = True)

          
        return Response({
            "status": True,
            "message": "data fetch",
            "data" : serializer.data
        })