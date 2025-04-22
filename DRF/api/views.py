from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WeaponSerializer

from api.models import Weapon


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons,many=True)
#         # data = {'message' : 'Привет!'}
#         return Response(ser.data)
#     if request.method == 'POST':
#         pass

# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         # data = {'message' : 'Привет!'}
#         return Response(ser.data)
#     def post(self, request):
#         return Response({'status' : 'ok'})

class DemoView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def post(self, request):
        return Response({'status' : 'ok'})

class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

