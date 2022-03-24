from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.views import Response

from .serializers import PostSerilizer
from .serializers import post


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'john',
            'age': 23
        }

        return Response(data)

    def post(self, request, *arg, **kwargs):
        serializer = PostSerilizer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


# def test_view(request):
#     data = {
#         'nama': 'john',
#         'age': 23
#     }
#     return JsonResponse(data) # if list safe=False
