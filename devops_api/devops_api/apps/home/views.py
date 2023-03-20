import time

from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return HttpResponse("HOME")


class TestView(APIView):
    def get(self, request):
        return Response({"msg": "hello devops"})
