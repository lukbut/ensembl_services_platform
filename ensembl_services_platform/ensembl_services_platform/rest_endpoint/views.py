from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class GeneMatcher(APIView):
    """
    A view that returns genes matching the partial gene name passed as a parameter
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, display_name=None, species=None):
        return Response('Hello World')
